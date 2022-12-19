from datetime import datetime


def sample_responses(input_tex):
    user_message = str(input_tex).lower()

    if user_message in ("hello", "hi", "what's up"):
      return "hey! How's it going?"


    if user_message in ("who are you","who are you?"):
      return "I am  joscamBot!"

    if user_message in ("time","time?","date?","date"):
           now = datetime.now()
           date_time = now.strftime("%d,%m,%y, %H:%M:%s")
           return str(date_time)


    return "i don't understand you"



