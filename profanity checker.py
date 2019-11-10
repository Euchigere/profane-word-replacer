from profanityfilter import ProfanityFilter

#function to censor text
pf= ProfanityFilter()

def censor(text):
    '''censor all offensive words with *'''
    pf.set_censor("*")
    censored = pf.censor(text)
    return censored

text= input("Enter text here:" )

text= censor(text)

text

#sample text

'''Calling someone an “asshole” in Georgia or Alabama might upset some people, but in these states, it’s apparently fine to use “bitch”, “damn” or “shit” to express everyday frustration.  Maps of the US with geotagged data from Twitter show the popularity of curse words throughout the country. UK-based linguist Jack Grieve created the maps, and has been tweeting them out to show which words are used more in different regions.  Grieve, a professor of forensic linguistics at Aston University in the UK, conducted the research with Diansheng Guo and Alice Kasakoff of University of South Carolina and Andrea Nini, of Aston University.  The researchers collected nearly a billion tweets dating from October 2013 to November 2014, totaling nearly 9bn words. Red areas on the maps show high relative usage of swear words, and blue areas show less.  The maps reveal word preferences that tend to be clustered in certain areas, especially in the outer areas of the country. The mid- and north-western regions of the country show a little red for the words “asshole” and “darn” but remain mostly blue or beige for other, more harsh words.  The reds and blues indicating the use of the words “shit”, “bitch” and “damn” hardly change on the maps, showing the words are popular throughout the south, and somewhat into the north-east, but hardly used in the rest of the country.  California appears fairly neutral in curse word popularity, remaining beige or blue for most words. The state goes totally red for “fuck”.'''
