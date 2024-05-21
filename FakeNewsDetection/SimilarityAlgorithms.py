import textdistance as td

delimitator = '\n--------------------------------------------------------------------------------\n\n'

similar_text1 = 'Pope Francis used his annual Christmas Day message to rebuke Donald Trump without even mentioning his name. The Pope delivered his message just days after members of the United Nations condemned Trump s move to recognize Jerusalem as the capital of Israel. The Pontiff prayed on Monday for the  peaceful coexistence of two states within mutually agreed and internationally recognized borders. We see Jesus in the children of the Middle East who continue to suffer because of growing tensions between Israelis and Palestinians,  Francis said.  On this festive day, let us ask the Lord for peace for Jerusalem and for all the Holy Land. Let us pray that the will to resume dialogue may prevail between the parties and that a negotiated solution can finally be reached. The Pope went on to plead for acceptance of refugees who have been forced from their homes, and that is an issue Trump continues to fight against. Francis used Jesus for which there was  no place in the inn  as an analogy. Today, as the winds of war are blowing in our world and an outdated model of development continues to produce human, societal and environmental decline, Christmas invites us to focus on the sign of the Child and to recognize him in the faces of little children, especially those for whom, like Jesus,  there is no place in the inn,  he said. Jesus knows well the pain of not being welcomed and how hard it is not to have a place to lay one s head,  he added.  May our hearts not be closed as they were in the homes of Bethlehem. The Pope said that Mary and Joseph were immigrants who struggled to find a safe place to stay in Bethlehem. They had to leave their people, their home, and their land,  Francis said.  This was no comfortable or easy journey for a young couple about to have a child.   At heart, they were full of hope and expectation because of the child about to be born; yet their steps were weighed down by the uncertainties and dangers that attend those who have to leave their home behind. So many other footsteps are hidden in the footsteps of Joseph and Mary,  Francis said Sunday. We see the tracks of entire families forced to set out in our own day. We see the tracks of millions of persons who do not choose to go away, but driven from their land, leave behind their dear ones. Amen to that.Photo by Christopher Furlong/Getty Images.'
similar_text2 = 'Pope Francis used his periodical Christmas Day message to rebuke Donald Trump without even mentioning his name. The Pope delivered his message just days after members of the United Nations condemned Trump s move to recognize Jerusalem as the capital of the city Israel. The Pontiff prayed on Monday for the  peaceful coexistence of two countries within mutually agreed and internationally recognized borders. We see Jesus Christ in the children of the Middle East who continue to suffer because of growing tensions between Palestinians and and the Israelians,  Francis said.  On this festive day, let us question the Lord for peace for Jerusalem and for all the Holy Land. Let us pray that the will to resume dialogue may prevail between the parties and that a negotiated solution can finally be reached. The Pope went on to plead for acceptance of displaced persons who have been forced from their homes, and that is an issue Trump continues to fight against. Francis used Jesus for which there was  no place in the inn  as an analogy. Today, as the winds of war are blowing in our world and an outdated model of development continues to produce human, societal and environmental decline, Christmas invites us to focus on the sign of the Child and to recognize him in the faces of little children, especially those for whom, like Jesus,  there is no place in the inn,  he said. Jesus knows well the pain of not being welcomed and how hard it is not to have a place to lay one s head,  he added.  May our hearts not be closed as they were in the homes of Bethlehem. The Pope said that Mary and Joseph were immigrants who struggled to find a safe place to stay in Bethlehem. They had to leave their people, their home, and their land,  Francis said.  This was no comfortable or easy journey for a young couple about to have a child.   At heart, they were full of hope and expectation because of the child about to be born; yet their steps were weighed down by the uncertainties and dangers that attend those who have to leave their home behind. So many other footsteps are hidden in the footsteps of Joseph and Mary,  Francis said Sunday. We see the pathway of entire families forced to set out in our own day. We see the tracks of millions of persons who do not choose to go away, but driven from their land, leave behind their dear ones. Amen to that.Photo by Christopher Furlong/Getty Images.'

different_text1 = 'Pope Francis used his annual Christmas Day message to rebuke Donald Trump without even mentioning his name. The Pope delivered his message just days after members of the United Nations condemned Trump s move to recognize Jerusalem as the capital of Israel. The Pontiff prayed on Monday for the  peaceful coexistence of two states within mutually agreed and internationally recognized borders. We see Jesus in the children of the Middle East who continue to suffer because of growing tensions between Israelis and Palestinians,  Francis said.  On this festive day, let us ask the Lord for peace for Jerusalem and for all the Holy Land. Let us pray that the will to resume dialogue may prevail between the parties and that a negotiated solution can finally be reached. The Pope went on to plead for acceptance of refugees who have been forced from their homes, and that is an issue Trump continues to fight against. Francis used Jesus for which there was  no place in the inn  as an analogy. Today, as the winds of war are blowing in our world and an outdated model of development continues to produce human, societal and environmental decline, Christmas invites us to focus on the sign of the Child and to recognize him in the faces of little children, especially those for whom, like Jesus,  there is no place in the inn,  he said. Jesus knows well the pain of not being welcomed and how hard it is not to have a place to lay one s head,  he added.  May our hearts not be closed as they were in the homes of Bethlehem. The Pope said that Mary and Joseph were immigrants who struggled to find a safe place to stay in Bethlehem. They had to leave their people, their home, and their land,  Francis said.  This was no comfortable or easy journey for a young couple about to have a child.   At heart, they were full of hope and expectation because of the child about to be born; yet their steps were weighed down by the uncertainties and dangers that attend those who have to leave their home behind. So many other footsteps are hidden in the footsteps of Joseph and Mary,  Francis said Sunday. We see the tracks of entire families forced to set out in our own day. We see the tracks of millions of persons who do not choose to go away, but driven from their land, leave behind their dear ones. Amen to that.Photo by Christopher Furlong/Getty Images.'
different_text2 = r'Pope Francis didn\'t used his annual Christmas Day message to rebuke Joe Biden without even mentioning his first name. The Pope delivered his message just days after members of the United States condemned Trump s move to recognize Jerusalem as the capital of Israel and put him to jail. The Pontiff jerked on Tuesday for the sake of god coexistence of three cities within mutually agreed and internationally unrecognized borders. We see Putin in the adult of the Middle East who continue to being happy because of growing tensions between Israelis and Palestinians,  Francis mewed.  On this jerking day, let us fell the Lord for die for Jerusalem and for all the Holy Land. Let us help that the will to resume dialogue may get good between the parties and that a negotiated answer can\'t finally be arrived. The Lenin went on to plead for forgivness of refugees who have been forced from their homes to surrender, and that is an issue Iohannis continues to fight against. Francis used Jesus for learning which there was  no place in the inn  as an analogy. Today, as the winds of war are blowing in our world and an outdated model of development continues to produce human, societal and environmental decline, Christmas invites us to focus on the sign of the Child and to recognize him in the faces of little children, especially those for whom, like Jesus,  there is no place in the inn,  he said. Jesus knows well the pain of not being welcomed and how hard it is not to have a place to lay one s head,  he added.  May our hearts not be closed as they were in the homes of Bethlehem. The Pope said that Mary and Joseph were immigrants who struggled to find a safe place to stay in Bethlehem. They had to leave their people, their home, and their land,  Francis said.  This was no comfortable or easy journey for a young couple about to have a child.   At heart, they were full of hope and expectation because of the child about to be born; yet their steps were weighed down by the uncertainties and dangers that attend those who have to leave their home behind. So many other footsteps are hidden in the footsteps of Joseph and Mary,  Francis said Sunday. We see the tracks of entire families forced to set out in our own day. We see the tracks of millions of persons who do not choose to go away, but driven from their land, leave behind their dear ones. Amen to that.Photo by Christopher Furlong/Getty Images.'

a = "I was in Japan 48 hours ago"
b = "I was in Japan 2 days ago"

# HAMMING

# print("HAMMING")
#
# print("Similar: ")
# print(f"Not-normalized: {td.hamming(similar_text1, similar_text2)}")
# print(f"Normalized: {td.hamming.normalized_similarity(similar_text1, similar_text2)}")
#
# print("Different:")
# print(f"Not-normalized: {td.hamming(different_text1, different_text2)}")
# print(f"Normalized: {td.hamming.normalized_similarity(different_text1, different_text2)}")
#
# print("Japan:", {td.hamming.normalized_similarity(a, b)})
#
# print(delimitator)
#
# # LEVENSHTEIN
#
# print("LEVENSTHEIN")
#
# print("Similar: ")
# print(f"Not-normalized: {td.levenshtein(similar_text1, similar_text2)}")
# print(f"Normalized: {td.levenshtein.normalized_similarity(similar_text1, similar_text2)}")
#
# print("Different: ")
# print(f"Not-normalized: {td.levenshtein(different_text1, different_text2)}")
# print(f"Normalized: {td.levenshtein.normalized_similarity(different_text1, different_text2)}")
#
# print("Japan:", {td.levenshtein.normalized_similarity(a, b)})
#
# print(delimitator)
#
# # DAMERAU-LEVENSTHEIN
#
# print("DAMERAU-LEVENSTHEIN")
#
# print("Similar: ")
# print(f"Not-normalized: {td.damerau_levenshtein(similar_text1, similar_text2)}")
# print(f"Normalized: {td.damerau_levenshtein.normalized_similarity(similar_text1, similar_text2)}")
#
# print("Different: ")
# print(f"Not-normalized: {td.damerau_levenshtein(different_text1, different_text2)}")
# print(f"Normalized: {td.damerau_levenshtein.normalized_similarity(different_text1, different_text2)}")
#
# print("Japan:", {td.hamming.normalized_similarity(a, b)})
#
# print(delimitator)
#
# # JARO
#
# print("JARO")
#
# print("Similar: ", td.jaro(similar_text1, similar_text2))
# print("Different: ", td.jaro(different_text1, different_text2))
#
# print("Japan:", {td.jaro(a, b)})
#
# print(delimitator)
#
# # JARO-WINKLER
#
# print("JARO-WINKLER")
#
# print("Similar: ", td.jaro_winkler(similar_text1, similar_text2))
# print("Different: ", td.jaro_winkler(different_text1, different_text2))
#
# print("Japan:", {td.jaro_winkler(a, b)})
#
#
# print(delimitator)
#
# # SMITH-WATERMAN
#
# print("SMITH-WATERMAN")
#
# print("Similar: ", td.smith_waterman(similar_text1, similar_text2))
# print("Different: ", td.smith_waterman(different_text1, different_text2))
#
# print("Japan:", {td.smith_waterman(a, b)})
#
# print(delimitator)
#
# # JACCARD
#
# print("JACCARD")
#
# print("Similar: ", td.jaccard(similar_text1.split(), similar_text2.split()))
# print("Different: ", td.jaccard(different_text1.split(), different_text2.split()))
#
# print("SimilarNOSPLIT: ", td.jaccard(similar_text1, similar_text2))
# print("DifferentNOSPLIT: ", td.jaccard(different_text1, different_text2))
#
# print("SimilarJAPAN: ", td.jaccard(a.split(), b.split()))
#
#
# print(delimitator)
#
# # SORENSEN-DICE
#
# print("SORENSEN-DICE")
#
# print("Similar: ", td.sorensen(similar_text1.split(), similar_text2.split()))
# print("Different: ", td.sorensen(different_text1.split(), different_text2.split()))
#
# print("Japan:", {td.sorensen(a, b)})
#
# print(delimitator)

# TVERSKY

print("TVERSKY")

tversky = td.Tversky(ks=(0.5, 0.5))
print("Similar: ", tversky(similar_text1.split(), similar_text2.split()))
print("Different: ", tversky(different_text1.split(), different_text2.split()))

print("Japan:", {tversky(a, b)})

print(delimitator)

# OVERLAP

# print("OVERLAP")
#
# print("Similar: ", td.overlap(similar_text1.split(), similar_text2.split()))
# print("Different: ", td.overlap(different_text1.split(), different_text2.split()))
#
# print("Japan:", {td.overlap(a, b)})
#
# print(delimitator)
#
# # COSINE
#
# print("COSINE")
#
# print("Similar: ", td.cosine(similar_text1.split(), similar_text2.split()))
# print("Different: ", td.cosine(different_text1.split(), different_text2.split()))
#
# print("Japan:", {td.cosine(a, b)})
#
# print(delimitator)
#
#
# # ?????? (Below)
#
# # RATCLIFF-OBERSHELP
#
# print("RATCLIFF-OBERSHELP")
#
# s1, s2 = "RO PATTERN MATCHING", "RO PRACTICE"
# td.ratcliff_obershelp(s1, s2), td.ratcliff_obershelp(s2, s1), len(s1), len(s2)
#
# print(delimitator)
#
# # LCS
#
# print("LCS")
#
# s1, s2 = "RO PATTERN MATCHING", "RO PRACTICE"
# td.lcsstr(s1, s2), td.lcsseq(s2, s1), td.lcsseq(s2, s1)
# td.lcsstr.normalized_similarity(s1, s2), td.lcsseq.normalized_similarity(s1, s2)
#
# print(delimitator)
