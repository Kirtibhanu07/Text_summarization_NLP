#!/usr/bin/env python
# coding: utf-8

# ## Text Summarization

# In[1]:


text="""Warren Edward Buffett is an American investor, business tycoon, philanthropist, and the chairman and CEO of Berkshire Hathaway. He is considered one of the most successful investors in the world and has a net worth of over US$85.6 billion as of December 2020,making him the world's fourth-wealthiest person. Buffett was born in Omaha, Nebraska. He developed an interest in business and investing in his youth, eventually entering the Wharton School of the University of Pennsylvania in 1947 before transferring to and graduating from the University of Nebraska at 19. He went on to graduate from Columbia Business School, where he molded his investment philosophy around the concept of value investing pioneered by Benjamin Graham. He attended New York Institute of Finance to focus his economics background and soon after began various business partnerships, including one with Graham. He created Buffett Partnership, Ltd in 1956 and his firm eventually acquired a textile manufacturing firm called Berkshire Hathaway, assuming its name to create a diversified holding company. In 1978, Charlie Munger joined Buffett as vice-chairman.
Buffett has been the chairman and largest shareholder of Berkshire Hathaway since 1970. He has been referred to as the "Oracle" or "Sage" of Omaha by global media.He is noted for his adherence to value investing, and his personal frugality despite his immense wealth.Research published at the University of Oxford characterizes Buffett's investment methodology as falling within "founder centrism", defined by a deference to managers with a founder's mindset, an ethical disposition towards the shareholder collective, and an intense focus on exponential value creation. Essentially, Buffett's concentrated investments shelter managers from the short-term pressures of the market.Buffett is a notable philanthropist, having pledged to give away 99 percent of his fortune to philanthropic causes, primarily via the Bill & Melinda Gates Foundation. He founded The Giving Pledge in 2009 with Bill Gates, whereby billionaires pledge to give away at least half of their fortunes."""


# In[2]:


text


# In[3]:


len(text)


# In[4]:


import spacy
from spacy.lang.en.stop_words import STOP_WORDS


# In[5]:


from string import punctuation


# In[7]:


punc=punctuation


# In[8]:


punc


# In[9]:


nlp=spacy.load("en_core_web_sm")


# In[10]:


doc=nlp(text)


# In[11]:


tokens=[token.text for token in doc]
print(tokens)


# In[12]:


punc=punc+'\n'


# In[13]:


punc


# ## Text cleaning

# In[17]:


word_freq={}
stop_words=list(STOP_WORDS)
for word in doc:
    if word.text.lower() not in stop_words:
        if word.text.lower() not in punc:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+= 1


# In[18]:


word_freq


# In[21]:


max_freq= max(word_freq.values())


# In[22]:


for word in word_freq.keys():
    word_freq[word]=word_freq[word]/max_freq


# In[23]:


word_freq


# ## Sentence tokenization

# In[25]:


sent_tokens=[sent for sent in doc.sents]
print(sent_tokens)


# In[26]:


sent_score={}


# In[29]:


for sent in sent_tokens:
    for word in sent:
        if word.text.lower() in word_freq.keys():
            if sent not in sent_score.keys():
                sent_score[sent]= word_freq[word.text.lower()]
            else:
                sent_score[sent]+=word_freq[word.text.lower()]


# In[31]:


print(sent_score)


# ## selecting 30% of max scoring sentence
# 

# In[32]:


from heapq import nlargest


# In[56]:


len(sent_score)*0.25


# ## getting 5 sentences

# In[57]:


summary=nlargest(n=4,iterable=sent_score,key=sent_score.get)


# In[58]:


summary


# In[59]:


final=[word.text for word in summary]


# In[60]:


print(final)


# In[61]:


summary=" ".join(final)


# In[62]:


print(summary)


# In[63]:


len(summary)


# In[64]:


len(summary)/len(text)


# In[ ]:




