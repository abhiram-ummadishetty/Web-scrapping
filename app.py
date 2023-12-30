import streamlit as st
import time
import datetime
import postuploader as pu
import csv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()


def save_uploaded_file(file):
    """Saves the uploaded file to the Streamlit session state."""
    with open(f'images/{file.name}', "wb") as f:
        f.write(file.read())



def schedule_postOnTime(timePost,Posts):
    with open("schedule_post.csv","r+") as f:
        myDataList = f.readlines()
        TimePostList = []
        for line in myDataList:
            entry = line.split(',')
            TimePostList.append(entry[0])
        if timePost not in TimePostList:
            f.writelines(f'\n{timePost},{list(Posts)}')



def schedule_postOnTime(timePost,Posts,caption):
    file = open('schedule_post.csv', 'r+',newline='',encoding='utf-8', errors='ignore')

    with file:
        # identifying header
        header = ['Time', 'Posts', 'Caption']
        writer = csv.DictWriter(file, fieldnames=header)
        # writing data row-wise into the csv file
        myDataList = file.readlines()
        TimePostList = []
        for line in myDataList:
            entry = line.split(',')
            TimePostList.append(entry[0])
        if timePost not in TimePostList:
            writer.writerow({'Time': timePost,
                             'Posts': Posts,
                             'Caption': caption})


def caption_generator():
    llm = OpenAI(temperature=0.7)
    captionGen = llm("write a caption of for instagram post which is trendy and classic")
    return captionGen

def post_auto():
    driver,length,upload_files = pu.connecion_est()
    pu.login("test_sele8", "@A012345", driver)
    pu.post(driver,upload_files,length)


now = time.localtime()
h = time.strftime("%H",now)
m = time.strftime("%M",now)

st.title("Instagram Post Automation")

st.subheader("Choose the images to be posted")

images = st.file_uploader("Upload images", accept_multiple_files=True)

print(images)
posts =[]

for img in images:
    if img is not None:
        print(img.name)
        save_uploaded_file(img)
        posts.append(img.name)


t = st.time_input('Schedule post at ', datetime.time(int(h), int(m)))
st.write('Scheduled post at', t)
generate = st.button("generate Caption")
if generate:
    caption = caption_generator()
txt = st.text_area(
    "Caption (changes can be made)",
    f"{caption}, (...)",
     )

st.write(f'You wrote {len(txt)} characters.')
sched = st.button("Schedule Task")
if sched:
    schedule_postOnTime(t,posts,str(txt))








    # for img in images:
    #     schedule.every().day.at(str(t)).do(post_auto())
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)



