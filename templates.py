import base64


def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


# Convert images to base64
user_avatar_base64 = get_base64_image("images/user_avatar.png")
bot_avatar_base64 = get_base64_image("images/bot_avatar.png")


def user_template(message):
    return f'''
    <div class="chat-message user">
        <div class="avatar">
            <img src="data:image/png;base64,{user_avatar_base64}">
        </div>    
        <div class="message">{message}</div>
    </div>
    '''


def bot_template(message):
    return f'''
    <div class="chat-message bot">
        <div class="avatar">
            <img src="data:image/png;base64,{bot_avatar_base64}" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
        </div>
        <div class="message">{message}</div>
    </div>
    '''


# CSS
css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''
