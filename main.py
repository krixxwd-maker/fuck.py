import requests
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

def approval():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def raj_logo():
    logo = r"""
██╗  ██╗██████╗ ██╗██╗  ██╗
██║ ██╔╝██╔══██╗██║╚██╗██╔╝
█████╔╝ ██████╔╝██║ ╚███╔╝
██╔═██╗ ██╔══██╗██║ ██╔██╗
██║  ██╗██║  ██║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝

          KRIX XWD
    """

    print(Fore.MAGENTA + Style.BRIGHT + logo)

def show_termux_message():
    termux_message = r"""
╔═══════════════════════════════════════════════════════════════════════════╗
║  OWNER      : KRIX XWD                                                   ║
║  TEAM       : BROTHER HOOD RULEX                                         ║
║  TOOL       : MULTI TOKEN CONVO                                          ║
║  GITHUB     : KRIX-XWD                                                   ║
║  WHATSAPP   : +918708206094                                              ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""
    print(Fore.GREEN + Style.BRIGHT + termux_message)

def fetch_profile_name(access_token):
    try:
        response = requests.get(
            "https://graph.facebook.com/me",
            params={"access_token": access_token}
        )
        response.raise_for_status()
        return response.json().get("name", "Unknown")
    except:
        return "Unknown"

def fetch_target_name(target_id, access_token):
    try:
        response = requests.get(
            f"https://graph.facebook.com/{target_id}",
            params={"access_token": access_token}
        )
        response.raise_for_status()
        return response.json().get("name", "Unknown Target")
    except:
        return "Unknown Target"

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):

    with open(messages_file, "r") as file:
        messages = file.readlines()

    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    token_profiles = {
        token: fetch_profile_name(token)
        for token in tokens
    }

    target_profile_name = fetch_target_name(
        target_id,
        tokens[0]
    )

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    while True:
        for message_index, message in enumerate(messages):

            token_index = message_index % len(tokens)
            access_token = tokens[token_index]

            sender_name = token_profiles.get(
                access_token,
                "Unknown Sender"
            )

            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"

            parameters = {
                "access_token": access_token,
                "message": full_message
            }

            try:
                response = requests.post(
                    url,
                    json=parameters,
                    headers=headers
                )

                response.raise_for_status()

                current_time = time.strftime(
                    "%Y-%m-%d %I:%M:%S %p"
                )

                print(Fore.GREEN + "\n" + "─" * 70)
                print(Fore.CYAN + f"[✔] Message {message_index + 1} Sent")
                print(Fore.YELLOW + f"[👤] Sender : {sender_name}")
                print(Fore.MAGENTA + f"[📩] Target : {target_profile_name}")
                print(Fore.LIGHTGREEN_EX + f"[📨] Msg : {full_message}")
                print(Fore.LIGHTBLUE_EX + f"[⏰] Time : {current_time}")
                print(Fore.GREEN + "─" * 70)

            except requests.exceptions.RequestException:
                continue

            time.sleep(speed)

        print(Fore.CYAN + "\n[+] Restarting Message Loop...\n")

def main():

    approval()
    raj_logo()
    show_termux_message()

    tokens_file = input(
        Fore.GREEN + "[+] TOKENS FILE : "
    ).strip()

    target_id = input(
        Fore.YELLOW + "[+] TARGET ID : "
    ).strip()

    messages_file = input(
        Fore.YELLOW + "[+] MESSAGE FILE : "
    ).strip()

    haters_name = input(
        Fore.YELLOW + "[+] NAME : "
    ).strip()

    speed = float(input(
        Fore.GREEN + "[+] SPEED : "
    ).strip())

    send_messages(
        tokens_file,
        target_id,
        messages_file,
        haters_name,
        speed
    )

if __name__ == "__main__":
    main()
