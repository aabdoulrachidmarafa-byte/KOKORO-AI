def kokoro_ai(message):
    message = message.lower().strip()

    if message in ["bonjour", "salut", "slt", "hello"]:
        return "🤖❤️ KOKORO AI : Bonjour ! Je suis là. Que puis-je faire pour toi ?"

    if message in ["qui es-tu", "qui es tu", "tu es qui"]:
        return "🤖 Je suis KOKORO AI, ton assistant Otaku."

    if message in ["aide", "help"]:
        return """🤖 KOKORO AI — MENU

👋 bonjour
🤖 qui es-tu
🎮 jeux
🏆 classement
📜 règles"""

    if message == "jeux":
        return "🎮 KOKORO AI : Les jeux arrivent bientôt !"

    return "🤖❤️ KOKORO AI : Je n'ai pas encore compris ce message."


# Petit test
print(kokoro_ai("bonjour"))
