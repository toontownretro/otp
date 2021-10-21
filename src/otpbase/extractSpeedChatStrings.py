from otp.otpbase.OTPLocalizer import SpeedChatStaticText, SpeedChatStaticTextToontown, SpeedChatStaticTextPirates, CustomSCStrings

# this script prints all static speedchat strings

msgs = set()

msgs.update(list(SpeedChatStaticText.values()))
msgs.update(list(SpeedChatStaticTextToontown.values()))
msgs.update(list(SpeedChatStaticTextPirates.values()))
msgs.update(list(CustomSCStrings.values()))

print('=== START SC STRINGS ===')

for msg in msgs:
    if len(msg):
        print(msg)
    
