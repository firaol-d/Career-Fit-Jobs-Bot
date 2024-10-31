import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import TOKEN, JOB_CATEGORIES
from database import add_user, update_user_preferences, get_user_preferences, add_pending_user
from policy import get_privacy_policy_url
from message_formatter import create_job_update, create_promotion_banner
from telegram.error import BadRequest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MAX_PREFERENCES = 15

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    is_new_user = add_user(user.id)
    
    privacy_url = get_privacy_policy_url()
    welcome_message = (
        f"👋 Welcome {user.first_name}!\n\n"
        "Let's set up your job preferences.\n\n"
        f"Please read our Privacy Policy:\n{privacy_url}"
    )
    await update.message.reply_text(welcome_message)
    
    await show_preference_menu(update, context)

async def preferences(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await show_preference_menu(update, context)

async def show_preference_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    user_preferences = get_user_preferences(user_id)
    
    keyboard = []
    row = []
    for i, category in enumerate(JOB_CATEGORIES, 1):
        icon = "✅" if category in user_preferences else "⬜️"
        row.append(InlineKeyboardButton(f"{icon} {category}", callback_data=f"pref_{category.lower().replace(' ', '_').replace('/', '_')}"))
        
        if i % 3 == 0 or i == len(JOB_CATEGORIES):
            keyboard.append(row)
            row = []
    
    keyboard.append([InlineKeyboardButton("Submit", callback_data="pref_submit")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = (f"Please select up to {MAX_PREFERENCES} job preferences:\n"
               f"(You have selected {len(user_preferences)}/{MAX_PREFERENCES})")
    
    if update.callback_query:
        await update.callback_query.edit_message_text(text=message, reply_markup=reply_markup)
    else:
        await update.message.reply_text(text=message, reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    
    if query.data == "pref_submit":
        await submit_preferences(update, context)
    else:
        category = query.data.replace("pref_", "").replace("_", " ").title()
        current_preferences = set(get_user_preferences(user_id))
        
        if category in current_preferences:
            current_preferences.remove(category)
        elif len(current_preferences) < MAX_PREFERENCES:
            current_preferences.add(category)
        else:
            await query.answer(f"You can only select up to {MAX_PREFERENCES} preferences. Please remove one before adding another.", show_alert=True)
            return
        
        update_user_preferences(user_id, list(current_preferences))
        await show_preference_menu(update, context)

async def submit_preferences(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    preferences = get_user_preferences(user_id)
    formatted_preferences = "\n".join([f"• {pref}" for pref in preferences])
    message = f"Your preferences have been updated:\n\n{formatted_preferences}"
    await update.callback_query.edit_message_text(message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "✨ *Career Fit Job Bot*\n\n"
        "🔍 *Available Commands:*\n"
        "• /start - Start the bot, Privacy Policy & set preferences\n"
        "• /preferences - Update your job categories\n"
        "• /help - Show this help message\n\n"
        "📬 *Updates Schedule:*\n"
        "You'll receive job matches 3 times daily\n\n"
        "💡 *Need Help?*\n"
        "Contact: @cfjsupport"
    )
    await update.message.reply_text(help_text)

async def send_job_updates(context: ContextTypes.DEFAULT_TYPE) -> None:
    # Implement the logic to send job updates here
    # This function will be called every 8 hours by the job queue
    pass

def setup_handlers(application: Application) -> None:
    """Setup bot handlers"""
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("preferences", preferences))
    application.add_handler(CallbackQueryHandler(button))
    # Add other handlers here

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    setup_handlers(application)

    application.run_polling()

if __name__ == '__main__':
    main()
