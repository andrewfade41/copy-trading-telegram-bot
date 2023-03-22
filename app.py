import logging
import csv
import ccxt
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

support_url = "https://t.me/+bJiAp1n4nYNlMmRk"
keyboard = [
        [InlineKeyboardButton("✅ Your bot is Active",callback_data="test"),],
        [
            InlineKeyboardButton("🤵 Traders", callback_data="traders"),
            InlineKeyboardButton("⚙️ Configure", callback_data="configure"),
        ],
        [
            InlineKeyboardButton("💵 Check", callback_data="check"),
            InlineKeyboardButton("📢 Channels", callback_data="channels"),
        ],
        [
            InlineKeyboardButton(text="👨‍💻 Support", url=support_url),
        ]
    ]
reply_markup = InlineKeyboardMarkup(keyboard)

def main_menu_keyboard(user):
    if check_user(user):
        global reply_markup
    else:
        keyboard = [
            [InlineKeyboardButton(text = "👨‍💻If you made the payment contact with support.👨‍💻", url=support_url),],
            [
                InlineKeyboardButton("🤵 Traders", callback_data="test"),
                InlineKeyboardButton("⚙️ Configure", callback_data="test"),
            ],
            [
                InlineKeyboardButton("💵 Check", callback_data="test"),
                InlineKeyboardButton("📢 Channels", callback_data="test"),
            ],
            [
                InlineKeyboardButton(text="👨‍💻 Support", url=support_url),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def check_user(user):
    with open("followers.csv", "r", encoding = "utf-8") as f:
        my_file = list(csv.reader(f))[1:]

    for line in my_file:
        if user == line[0]:
            return True
    return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    user = update.effective_user
    userid = str(user.id)
    logger.info("User %s started the conversation.", user.first_name)

    if check_user(userid):
        text = "🤖Welcome to the Crypto Pilot CopyTrading Bot🤖"
    else:
        text ="🤖Welcome to the Crypto Pilot CopyTrading Bot🤖\n✋ Your bot is NOT Active."

    await update.message.reply_text(text, reply_markup=main_menu_keyboard(userid))




async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""

    query = update.callback_query

    await query.answer()
    user = update.effective_user
    userid = str(user.first_name)
    await query.edit_message_text(text="🤖Welcome to the Crypto Pilot CopyTrading Bot🤖", reply_markup=main_menu_keyboard(userid))


async def traders_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    user = update.effective_user
    userid = str(user.first_name)
    print("user id", userid, type(userid))
    await query.answer()
    keyboard = [
            [InlineKeyboardButton("🛑STOP FOLLOWING🛑", callback_data= "no one"),],
            [InlineKeyboardButton("✅ btc-to-moon", callback_data= "btc-to-moon"),],
            [InlineKeyboardButton("✅ CnTraderT", callback_data="CnTraderT")],
            [InlineKeyboardButton("✅ StellarMom", callback_data="StellarMom")],
            [InlineKeyboardButton("✅ wreckord741741", callback_data="wreckord741741")],
            [InlineKeyboardButton("✅ BeraGrizzly", callback_data="BeraGrizzly")],
            [InlineKeyboardButton("🔙 Return to main menu", callback_data="mainmenu"),],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=f"CHOOSE YOUR TRADER {userid}", reply_markup=reply_markup
    )

def leverage(user):
    with open("followers.csv", "r", encoding = "utf-8") as f:
        my_file = list(csv.reader(f))[1:]

    for line in my_file:
        if user == line[0]:
            return line[5]

def balance(user):
    with open("followers.csv", "r", encoding = "utf-8") as f:
        my_file = list(csv.reader(f))[1:]

    for line in my_file:
        if user == line[0]:
            return line[4]

async def channels_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    user = update.effective_user
    userid = str(user.id)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton(f"📈 Marzell Trade Signals ™️", url="https://t.me/+whcBMxlMx9RlNDc0")],
        [InlineKeyboardButton(f"𝗠𝗮𝗿𝘇𝗲𝗹𝗹 𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗦𝗶𝗴𝗻𝗮𝗹𝘀 ™️", url= "t.me/MarzellOfficial"),],
         [InlineKeyboardButton("🔙 Return to main menu", callback_data="mainmenu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="You can join the channels", reply_markup=reply_markup
    )
async def configure_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    user = update.effective_user
    userid = str(user.id)
    await query.answer()
    keyboard = [
        [InlineKeyboardButton(f"Leverage: {leverage(userid)}", callback_data="leverage_menu")],
        [InlineKeyboardButton(f"Percentage of Balance: {balance(userid)}", callback_data="balance_menu"),],
         [InlineKeyboardButton("🔙 Return to main menu", callback_data="mainmenu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Exchange Configuration", reply_markup=reply_markup
    )

async def leverage_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    query = update.callback_query
    user = update.effective_user
    await query.answer()
    keyboard = [ [
            InlineKeyboardButton("Follow Lead's Leverage", callback_data="lead"),
           
        ],
        [
            InlineKeyboardButton("1 X", callback_data="leverage1"),
            InlineKeyboardButton("2 X", callback_data="leverage2"),
        ],[
            InlineKeyboardButton("3 X", callback_data="leverage3"),
            InlineKeyboardButton("4 X", callback_data="leverage4"),
        ],
                [
            InlineKeyboardButton("5 X", callback_data="leverage5"),
            InlineKeyboardButton("6 X", callback_data="leverage6"),
        ],
                [
            InlineKeyboardButton("7 X", callback_data="leverage7"),
            InlineKeyboardButton("8 X", callback_data="leverage8"),
        ],
                [
            InlineKeyboardButton("9 X", callback_data="leverage9"),
            InlineKeyboardButton("10 X", callback_data="leverage10"),
        ],
        [InlineKeyboardButton("🔙 Return to main menu", callback_data="mainmenu")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("Choose Leverage Value (1-10)", reply_markup=reply_markup)
def change_data(user, trader = None, leverage = None, balance =None):
    with open("followers.csv", "r", encoding = "utf-8") as f:
        my_file = list(csv.reader(f))

    for line in my_file[1:]:
        if user == line[0]:
            if trader:
                line[3] = trader
            elif leverage:
                line[5] = leverage
            elif balance:
                line[4] = balance
            break
    with open("followers.csv", "w", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(my_file)
    return

async def leverage_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    await query.answer()
    user = update.effective_user
    print(user, query.data)

    leverage = query.data
    if leverage != "lead":
        leverage = leverage[8:]
        text = f"You changed your leverage to {leverage}X"
    else:
        text = "Your leverage will be same with lead."
    userid = str(user.id)
    change_data(userid, leverage = leverage)
    await query.edit_message_text(text=text,reply_markup=reply_markup)    

async def check_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user = update.effective_user
    userid = str(user.id)
    with open("followers.csv", "r", encoding = "utf-8") as f:
        my_file = list(csv.reader(f))[1:]
    for line in my_file:
        if userid == line[0]:
            api_key = line[6]
            secret_key = line[7]
            leverage = line[5]
            margin = line[4]
            trader = line[3]
            username = line[1]
            break
    exchange = ccxt.bybit({
        'apiKey': api_key,
        'secret': secret_key,
        "headers": {"referer": "Vz000208"},
        })
    exchange.options['defaultType'] = 'future'
    balance = exchange.fetch_balance(params={"accountType":"UNIFIED"})
    amount = round(float(balance["USDT"]["total"]),4)
    
    text = f"Hello {username}.\nYour total balance is {amount} USDT.\nYour leverage is {leverage if leverage.isdigit() else 'same with lead'}.\nYour trade margin {margin}.\nYou are following {trader}"
    await query.edit_message_text(text=text,reply_markup=reply_markup)    

async def balance_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query
    user = update.effective_user
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1 %", callback_data="balance1"),
            InlineKeyboardButton("2 %", callback_data="balance2"),
        ],[
            InlineKeyboardButton("3 %", callback_data="balance3"),
            InlineKeyboardButton("4 %", callback_data="balance4"),
        ],
                [
            InlineKeyboardButton("5 %", callback_data="balance5"),
            InlineKeyboardButton("6 %", callback_data="balance6"),
        ],
                [
            InlineKeyboardButton("7 %", callback_data="balance7"),
            InlineKeyboardButton("8 %", callback_data="balance8"),
        ],
                [
            InlineKeyboardButton("9 %", callback_data="balance9"),
            InlineKeyboardButton("10 %", callback_data="balance10"),
        ],
        [InlineKeyboardButton("🔙 Return to main menu", callback_data="mainmenu")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("Choose Percentage of Balance Value for each position (1-10)", reply_markup=reply_markup)

async def balance_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query

    await query.answer()
    user = update.effective_user
    print(user, query.data)

    balance = query.data[7:]
    userid = str(user.id)
    change_data(userid, balance = balance)

    await query.edit_message_text(text=f"Bot will use {balance}% of your total balance for each position.",reply_markup=reply_markup)    


async def traders_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    await query.answer()
    user = update.effective_user
    print(user, query.data)

    option = query.data
    userid = str(user.id)
    change_data(userid, trader=option)
    await query.edit_message_text(text=f"You are following {option}.",reply_markup=reply_markup)
 
def main() -> None:

    application = Application.builder().token("").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(start_over, pattern="mainmenu"))
    application.add_handler(CallbackQueryHandler(traders_menu, pattern='traders'))
    application.add_handler(CallbackQueryHandler(channels_menu, pattern='channels'))
    application.add_handler(CallbackQueryHandler(configure_menu, pattern='configure'))
    application.add_handler(CallbackQueryHandler(check_menu, pattern='check'))
    application.add_handler(CallbackQueryHandler(traders_button, pattern= "btc-to-moon"))
    application.add_handler(CallbackQueryHandler(traders_button, pattern='CnTraderT'))
    application.add_handler(CallbackQueryHandler(traders_button, pattern="StellarMom"))
    application.add_handler(CallbackQueryHandler(traders_button, pattern='wreckord741741'))
    application.add_handler(CallbackQueryHandler(traders_button, pattern='BeraGrizzly'))
    application.add_handler(CallbackQueryHandler(traders_button, pattern='no one'))
    application.add_handler(CallbackQueryHandler(leverage_menu, pattern='leverage_menu'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='lead'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='leverage1'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='leverage2'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='leverage3'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='leverage4'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='leverage5'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='leverage6'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='leverage7'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='leverage8'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='leverage9'))
    application.add_handler(CallbackQueryHandler(leverage_button, pattern='leverage10'))
    application.add_handler(CallbackQueryHandler(balance_menu, pattern='balance_menu'))
    application.add_handler(CallbackQueryHandler(balance_button, pattern='balance1'))
    application.add_handler(CallbackQueryHandler(balance_button, pattern='balance2'))
    application.add_handler(CallbackQueryHandler(balance_button, pattern='balance3'))
    application.add_handler(CallbackQueryHandler(balance_button, pattern='balance4'))
    application.add_handler(CallbackQueryHandler(balance_button, pattern='balance5'))
    application.add_handler(CallbackQueryHandler(balance_button, pattern='balance6'))
    application.add_handler(CallbackQueryHandler(balance_button, pattern='balance7'))
    application.add_handler(CallbackQueryHandler(balance_button, pattern='balance8'))
    application.add_handler(CallbackQueryHandler(balance_button, pattern='balance9'))
    application.add_handler(CallbackQueryHandler(balance_button, pattern='balance10'))

    application.run_polling()


if __name__ == "__main__":
    main()
