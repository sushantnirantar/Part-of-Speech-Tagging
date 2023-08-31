###################################
# CS B551 Spring 2021, Assignment #3
#
# Your names and user ids:Sushant Nirantar
#
# (Based on skeleton code by D. Crandall)
#


import random
import math


# We've set up a suggested code structure, but feel free to change it. Just
# make sure your code still works with the label.py and pos_scorer.py code
# that we've supplied.
#

def rand_pos(sentence):
        lst=[]
        pos=["det","adj","adp","adv","noun","num","verb","conj","prt","pron","x","."]
        for i in range(len(sentence)):
            lst.append(random.choice(pos))
        return lst
def cpy_lst(lst):
    lst1=[]
    for i in lst:
        lst1.append(i)
    return lst1

class Word:
    def __init__(self,word,emission,transition,initial,level,parent):
        self.word=word
        self.emission=emission
        self.transition=transition
        self.initial=initial
        self.level=level
        self.scores=[]
        for i in self.emission:
            if(self.word in i):
                self.scores.append(i[self.word])
            else:
                self.scores.append(0.000000000000000000000001)
        self.parent=parent
        self.det_string=["det"]
        self.adj_string=["adj"]
        self.adp_string=["adp"]
        self.adv_string=["adv"]
        self.noun_string=["noun"]
        self.num_string=["num"]
        self.verb_string=["verb"]
        self.conj_string=["conj"]
        self.prt_string=["prt"]
        self.pron_string=["pron"]
        self.x_string=["x"]
        self.dot_string=["."]
        self.result_holder=[]
        self.maxi=0

    def compute_scores(self):
        if(self.level==0):
            self.scores[0]=(self.scores[0]*self.initial["DET"])
            self.scores[1]=(self.scores[1]*self.initial["ADJ"])
            self.scores[2]=(self.scores[2]*self.initial["ADP"])
            self.scores[3]=(self.scores[3]*self.initial["ADV"])
            self.scores[4]=(self.scores[4]*self.initial["NOUN"])
            self.scores[5]=(self.scores[5]*self.initial["NUM"])
            self.scores[6]=(self.scores[6]*self.initial["VERB"])
            self.scores[7]=(self.scores[7]*self.initial["CONJ"])
            self.scores[8]=(self.scores[8]*self.initial["PRT"])
            self.scores[9]=(self.scores[9]*self.initial["PRON"])
            self.scores[10]=(self.scores[10]*self.initial["X"])
            self.scores[11]=(self.scores[11]*self.initial["."])
            
            self.result_holder.append(self.det_string)
            
            self.result_holder.append(self.adj_string)
            
            self.result_holder.append(self.adp_string)
            
            self.result_holder.append(self.adv_string)
            
            self.result_holder.append(self.noun_string)
            
            self.result_holder.append(self.num_string)
            
            self.result_holder.append(self.verb_string)
            
            self.result_holder.append(self.conj_string)
            
            self.result_holder.append(self.prt_string)
            
            self.result_holder.append(self.pron_string)
            
            self.result_holder.append(self.x_string)
            
            self.result_holder.append(self.dot_string)
            self.maxi=self.scores.index(max(self.scores))
            
        else:
            #print(self.scores)
            #print(self.parent.scores)
            lst1=cpy_lst(self.parent.scores)
            lst1[0]=lst1[0]*max(0.0000000000000001,self.transition["DET-DET"])
            lst1[1]=lst1[1]*max(0.0000000000000001,self.transition["ADJ-DET"])
            lst1[2]=lst1[2]*max(0.0000000000000001,self.transition["ADP-DET"])
            lst1[3]=lst1[3]*max(0.0000000000000001,self.transition["ADV-DET"])
            lst1[4]=lst1[4]*max(0.0000000000000001,self.transition["NOUN-DET"])
            lst1[5]=lst1[5]*max(0.0000000000000001,self.transition["NUM-DET"])
            lst1[6]=lst1[6]*max(0.0000000000000001,self.transition["VERB-DET"])
            lst1[7]=lst1[7]*max(0.0000000000000001,self.transition["CONJ-DET"])
            lst1[8]=lst1[8]*max(0.0000000000000001,self.transition["PRT-DET"])
            lst1[9]=lst1[9]*max(0.0000000000000001,self.transition["PRON-DET"])
            lst1[10]=lst1[10]*max(0.0000000000000001,self.transition["X-DET"])
            lst1[11]=lst1[11]*max(0.0000000000000001,self.transition[".-DET"])
            self.scores[0]=(self.scores[0]*max(lst1))
            maxindex=lst1.index(max(lst1))
            if(maxindex==0):
                self.det_string=self.parent.det_string+self.det_string
            elif(maxindex==1):
                self.det_string=self.parent.adj_string+self.det_string
            elif(maxindex==2):
                self.det_string=self.parent.adp_string+self.det_string
            elif(maxindex==3):
                self.det_string=self.parent.adv_string+self.det_string
            elif(maxindex==4):
                self.det_string=self.parent.noun_string+self.det_string
            elif(maxindex==5):
                self.det_string=self.parent.num_string+self.det_string
            elif(maxindex==6):
                self.det_string=self.parent.verb_string+self.det_string
            elif(maxindex==7):
                self.det_string=self.parent.conj_string+self.det_string
            elif(maxindex==8):
                self.det_string=self.parent.prt_string+self.det_string
            elif(maxindex==9):
                self.det_string=self.parent.pron_string+self.det_string
            elif(maxindex==10):
                self.det_string=self.parent.x_string+self.det_string
            elif(maxindex==11):
                self.det_string=self.parent.dot_string+self.det_string
            else:
                pass
            self.result_holder.append(self.det_string)

            lst2=cpy_lst(self.parent.scores)
            lst2[0]=lst2[0]*max(0.0000000000000001,self.transition["DET-ADJ"])
            lst2[1]=lst2[1]*max(0.0000000000000001,self.transition["ADJ-ADJ"])
            lst2[2]=lst2[2]*max(0.0000000000000001,self.transition["ADP-ADJ"])
            lst2[3]=lst2[3]*max(0.0000000000000001,self.transition["ADV-ADJ"])
            lst2[4]=lst2[4]*max(0.0000000000000001,self.transition["NOUN-ADJ"])
            lst2[5]=lst2[5]*max(0.0000000000000001,self.transition["NUM-ADJ"])
            lst2[6]=lst2[6]*max(0.0000000000000001,self.transition["VERB-ADJ"])
            lst2[7]=lst2[7]*max(0.0000000000000001,self.transition["CONJ-ADJ"])
            lst2[8]=lst2[8]*max(0.0000000000000001,self.transition["PRT-ADJ"])
            lst2[9]=lst2[9]*max(0.0000000000000001,self.transition["PRON-ADJ"])
            lst2[10]=lst2[10]*max(0.0000000000000001,self.transition["X-ADJ"])
            lst2[11]=lst2[11]*max(0.0000000000000001,self.transition[".-ADJ"])
            self.scores[1]=(self.scores[1]*max(lst2))
            maxindex1=lst2.index(max(lst2))
            if(maxindex1==0):
                self.adj_string=self.parent.det_string+self.adj_string
            elif(maxindex1==1):
                self.adj_string=self.parent.adj_string+self.adj_string
            elif(maxindex1==2):
                self.adj_string=self.parent.adp_string+self.adj_string
            elif(maxindex1==3):
                self.adj_string=self.parent.adv_string+self.adj_string
            elif(maxindex1==4):
                self.adj_string=self.parent.noun_string+self.adj_string
            elif(maxindex1==5):
                self.adj_string=self.parent.num_string+self.adj_string
            elif(maxindex1==6):
                self.adj_string=self.parent.verb_string+self.adj_string
            elif(maxindex1==7):
                self.adj_string=self.parent.conj_string+self.adj_string
            elif(maxindex1==8):
                self.adj_string=self.parent.prt_string+self.adj_string
            elif(maxindex1==9):
                self.adj_string=self.parent.pron_string+self.adj_string
            elif(maxindex1==10):
                self.adj_string=self.parent.x_string+self.adj_string
            elif(maxindex1==11):
                self.adj_string=self.parent.dot_string+self.adj_string
            else:
                pass
            self.result_holder.append(self.adj_string)

            lst3=cpy_lst(self.parent.scores)
            lst3[0]=lst3[0]*max(0.0000000000000001,self.transition["DET-ADP"])
            lst3[1]=lst3[1]*max(0.0000000000000001,self.transition["ADJ-ADP"])
            lst3[2]=lst3[2]*max(0.0000000000000001,self.transition["ADP-ADP"])
            lst3[3]=lst3[3]*max(0.0000000000000001,self.transition["ADV-ADP"])
            lst3[4]=lst3[4]*max(0.0000000000000001,self.transition["NOUN-ADP"])
            lst3[5]=lst3[5]*max(0.0000000000000001,self.transition["NUM-ADP"])
            lst3[6]=lst3[6]*max(0.0000000000000001,self.transition["VERB-ADP"])
            lst3[7]=lst3[7]*max(0.0000000000000001,self.transition["CONJ-ADP"])
            lst3[8]=lst3[8]*max(0.0000000000000001,self.transition["PRT-ADP"])
            lst3[9]=lst3[9]*max(0.0000000000000001,self.transition["PRON-ADP"])
            lst3[10]=lst3[10]*max(0.0000000000000001,self.transition["X-ADP"])
            lst3[11]=lst3[11]*max(0.0000000000000001,self.transition[".-ADP"])
            self.scores[2]=(self.scores[1]*max(lst3))
            maxindex2=lst3.index(max(lst3))
            if(maxindex2==0):
                self.adp_string=self.parent.det_string+self.adp_string
            elif(maxindex2==1):
                self.adp_string=self.parent.adj_string+self.adp_string
            elif(maxindex2==2):
                self.adp_string=self.parent.adp_string+self.adp_string
            elif(maxindex2==3):
                self.adp_string=self.parent.adv_string+self.adp_string
            elif(maxindex2==4):
                self.adp_string=self.parent.noun_string+self.adp_string
            elif(maxindex2==5):
                self.adp_string=self.parent.num_string+self.adp_string
            elif(maxindex2==6):
                self.adp_string=self.parent.verb_string+self.adp_string
            elif(maxindex2==7):
                self.adp_string=self.parent.conj_string+self.adp_string
            elif(maxindex2==8):
                self.adp_string=self.parent.prt_string+self.adp_string
            elif(maxindex2==9):
                self.adp_string=self.parent.pron_string+self.adp_string
            elif(maxindex2==10):
                self.adp_string=self.parent.x_string+self.adp_string
            elif(maxindex2==11):
                self.adp_string=self.parent.dot_string+self.adp_string
            else:
                pass
            self.result_holder.append(self.adp_string)

            lst4=cpy_lst(self.parent.scores)
            lst4[0]=lst4[0]*max(0.0000000000000001,self.transition["DET-ADV"])
            lst4[1]=lst4[1]*max(0.0000000000000001,self.transition["ADJ-ADV"])
            lst4[2]=lst4[2]*max(0.0000000000000001,self.transition["ADP-ADV"])
            lst4[3]=lst4[3]*max(0.0000000000000001,self.transition["ADV-ADV"])
            lst4[4]=lst4[4]*max(0.0000000000000001,self.transition["NOUN-ADV"])
            lst4[5]=lst4[5]*max(0.0000000000000001,self.transition["NUM-ADV"])
            lst4[6]=lst4[6]*max(0.0000000000000001,self.transition["VERB-ADV"])
            lst4[7]=lst4[7]*max(0.0000000000000001,self.transition["CONJ-ADV"])
            lst4[8]=lst4[8]*max(0.0000000000000001,self.transition["PRT-ADV"])
            lst4[9]=lst4[9]*max(0.0000000000000001,self.transition["PRON-ADV"])
            lst4[10]=lst4[10]*max(0.0000000000000001,self.transition["X-ADV"])
            lst4[11]=lst4[11]*max(0.0000000000000001,self.transition[".-ADV"])
            self.scores[3]=(self.scores[3]*max(lst4))
            maxindex3=lst4.index(max(lst4))
            if(maxindex3==0):
                self.adv_string=self.parent.det_string+self.adv_string
            elif(maxindex3==1):
                self.adv_string=self.parent.adj_string+self.adv_string
            elif(maxindex3==2):
                self.adv_string=self.parent.adp_string+self.adv_string
            elif(maxindex3==3):
                self.adv_string=self.parent.adv_string+self.adv_string
            elif(maxindex3==4):
                self.adv_string=self.parent.noun_string+self.adv_string
            elif(maxindex3==5):
                self.adv_string=self.parent.num_string+self.adv_string
            elif(maxindex3==6):
                self.adv_string=self.parent.verb_string+self.adv_string
            elif(maxindex3==7):
                self.adv_string=self.parent.conj_string+self.adv_string
            elif(maxindex3==8):
                self.adv_string=self.parent.prt_string+self.adv_string
            elif(maxindex3==9):
                self.adv_string=self.parent.pron_string+self.adv_string
            elif(maxindex3==10):
                self.adv_string=self.parent.x_string+self.adv_string
            elif(maxindex3==11):
                self.adv_string=self.parent.dot_string+self.adv_string
            else:
                pass
            self.result_holder.append(self.adv_string)

            lst5=cpy_lst(self.parent.scores)
            lst5[0]=lst5[0]*max(0.0000000000000001,self.transition["DET-NOUN"])
            lst5[1]=lst5[1]*max(0.0000000000000001,self.transition["ADJ-NOUN"])
            lst5[2]=lst5[2]*max(0.0000000000000001,self.transition["ADP-NOUN"])
            lst5[3]=lst5[3]*max(0.0000000000000001,self.transition["ADV-NOUN"])
            lst5[4]=lst5[4]*max(0.0000000000000001,self.transition["NOUN-NOUN"])
            lst5[5]=lst5[5]*max(0.0000000000000001,self.transition["NUM-NOUN"])
            lst5[6]=lst5[6]*max(0.0000000000000001,self.transition["VERB-NOUN"])
            lst5[7]=lst5[7]*max(0.0000000000000001,self.transition["CONJ-NOUN"])
            lst5[8]=lst5[8]*max(0.0000000000000001,self.transition["PRT-NOUN"])
            lst5[9]=lst5[9]*max(0.0000000000000001,self.transition["PRON-NOUN"])
            lst5[10]=lst5[10]*max(0.0000000000000001,self.transition["X-NOUN"])
            lst5[11]=lst5[11]*max(0.0000000000000001,self.transition[".-NOUN"])
            self.scores[4]=(self.scores[4]*max(lst5))
            maxindex4=lst5.index(max(lst5))
            if(maxindex4==0):
                self.noun_string=self.parent.det_string+self.noun_string
            elif(maxindex4==1):
                self.noun_string=self.parent.adj_string+self.noun_string
            elif(maxindex4==2):
                self.noun_string=self.parent.adp_string+self.noun_string
            elif(maxindex4==3):
                self.noun_string=self.parent.adv_string+self.noun_string
            elif(maxindex4==4):
                self.noun_string=self.parent.noun_string+self.noun_string
            elif(maxindex4==5):
                self.noun_string=self.parent.num_string+self.noun_string
            elif(maxindex4==6):
                self.noun_string=self.parent.verb_string+self.noun_string
            elif(maxindex4==7):
                self.noun_string=self.parent.conj_string+self.noun_string
            elif(maxindex4==8):
                self.noun_string=self.parent.prt_string+self.noun_string
            elif(maxindex4==9):
                self.noun_string=self.parent.pron_string+self.noun_string
            elif(maxindex4==10):
                self.noun_string=self.parent.x_string+self.noun_string
            elif(maxindex4==11):
                self.noun_string=self.parent.dot_string+self.noun_string
            else:
                pass
            self.result_holder.append(self.noun_string)

            lst6=cpy_lst(self.parent.scores)
            lst6[0]=lst6[0]*max(0.0000000000000001,self.transition["DET-NUM"])
            lst6[1]=lst6[1]*max(0.0000000000000001,self.transition["ADJ-NUM"])
            lst6[2]=lst6[2]*max(0.0000000000000001,self.transition["ADP-NUM"])
            lst6[3]=lst6[3]*max(0.0000000000000001,self.transition["ADV-NUM"])
            lst6[4]=lst6[4]*max(0.0000000000000001,self.transition["NOUN-NUM"])
            lst6[5]=lst6[5]*max(0.0000000000000001,self.transition["NUM-NUM"])
            lst6[6]=lst6[6]*max(0.0000000000000001,self.transition["VERB-NUM"])
            lst6[7]=lst6[7]*max(0.0000000000000001,self.transition["CONJ-NUM"])
            lst6[8]=lst6[8]*max(0.0000000000000001,self.transition["PRT-NUM"])
            lst6[9]=lst6[9]*max(0.0000000000000001,self.transition["PRON-NUM"])
            lst6[10]=lst6[10]*max(0.0000000000000001,self.transition["X-NUM"])
            lst6[11]=lst6[11]*max(0.0000000000000001,self.transition[".-NUM"])
            self.scores[5]=(self.scores[5]*max(lst6))
            maxindex5=lst6.index(max(lst6))
            if(maxindex5==0):
                self.num_string=self.parent.det_string+self.num_string
            elif(maxindex5==1):
                self.num_string=self.parent.adj_string+self.num_string
            elif(maxindex5==2):
                self.num_string=self.parent.adp_string+self.num_string
            elif(maxindex5==3):
                self.num_string=self.parent.adv_string+self.num_string
            elif(maxindex5==4):
                self.num_string=self.parent.noun_string+self.num_string
            elif(maxindex5==5):
                self.num_string=self.parent.num_string+self.num_string
            elif(maxindex5==6):
                self.num_string=self.parent.verb_string+self.num_string
            elif(maxindex5==7):
                self.num_string=self.parent.conj_string+self.num_string
            elif(maxindex5==8):
                self.num_string=self.parent.prt_string+self.num_string
            elif(maxindex5==9):
                self.num_string=self.parent.pron_string+self.num_string
            elif(maxindex5==10):
                self.num_string=self.parent.x_string+self.num_string
            elif(maxindex5==11):
                self.num_string=self.parent.dot_string+self.num_string
            else:
                pass
            self.result_holder.append(self.num_string)

            lst7=cpy_lst(self.parent.scores)
            lst7[0]=lst7[0]*max(0.0000000000000001,self.transition["DET-VERB"])
            lst7[1]=lst7[1]*max(0.0000000000000001,self.transition["ADJ-VERB"])
            lst7[2]=lst7[2]*max(0.0000000000000001,self.transition["ADP-VERB"])
            lst7[3]=lst7[3]*max(0.0000000000000001,self.transition["ADV-VERB"])
            lst7[4]=lst7[4]*max(0.0000000000000001,self.transition["NOUN-VERB"])
            lst7[5]=lst7[5]*max(0.0000000000000001,self.transition["NUM-VERB"])
            lst7[6]=lst7[6]*max(0.0000000000000001,self.transition["VERB-VERB"])
            lst7[7]=lst7[7]*max(0.0000000000000001,self.transition["CONJ-VERB"])
            lst7[8]=lst7[8]*max(0.0000000000000001,self.transition["PRT-VERB"])
            lst7[9]=lst7[9]*max(0.0000000000000001,self.transition["PRON-VERB"])
            lst7[10]=lst7[10]*max(0.0000000000000001,self.transition["X-VERB"])
            lst7[11]=lst7[11]*max(0.0000000000000001,self.transition[".-VERB"])
            self.scores[6]=(self.scores[6]*max(lst7))
            maxindex6=lst7.index(max(lst7))
            if(maxindex6==0):
                self.verb_string=self.parent.det_string+self.verb_string
            elif(maxindex6==1):
                self.verb_string=self.parent.adj_string+self.verb_string
            elif(maxindex6==2):
                self.verb_string=self.parent.adp_string+self.verb_string
            elif(maxindex6==3):
                self.verb_string=self.parent.adv_string+self.verb_string
            elif(maxindex6==4):
                self.verb_string=self.parent.noun_string+self.verb_string
            elif(maxindex6==5):
                self.verb_string=self.parent.num_string+self.verb_string
            elif(maxindex6==6):
                self.verb_string=self.parent.verb_string+self.verb_string
            elif(maxindex6==7):
                self.verb_string=self.parent.conj_string+self.verb_string
            elif(maxindex6==8):
                self.verb_string=self.parent.prt_string+self.verb_string
            elif(maxindex6==9):
                self.verb_string=self.parent.pron_string+self.verb_string
            elif(maxindex6==10):
                self.verb_string=self.parent.x_string+self.verb_string
            elif(maxindex6==11):
                self.verb_string=self.parent.dot_string+self.verb_string
            else:
                pass
            self.result_holder.append(self.verb_string)

            lst8=cpy_lst(self.parent.scores)
            lst8[0]=lst8[0]*max(0.0000000000000001,self.transition["DET-CONJ"])
            lst8[1]=lst8[1]*max(0.0000000000000001,self.transition["ADJ-CONJ"])
            lst8[2]=lst8[2]*max(0.0000000000000001,self.transition["ADP-CONJ"])
            lst8[3]=lst8[3]*max(0.0000000000000001,self.transition["ADV-CONJ"])
            lst8[4]=lst8[4]*max(0.0000000000000001,self.transition["NOUN-CONJ"])
            lst8[5]=lst8[5]*max(0.0000000000000001,self.transition["NUM-CONJ"])
            lst8[6]=lst8[6]*max(0.0000000000000001,self.transition["VERB-CONJ"])
            lst8[7]=lst8[7]*max(0.0000000000000001,self.transition["CONJ-CONJ"])
            lst8[8]=lst8[8]*max(0.0000000000000001,self.transition["PRT-CONJ"])
            lst8[9]=lst8[9]*max(0.0000000000000001,self.transition["PRON-CONJ"])
            lst8[10]=lst8[10]*max(0.0000000000000001,self.transition["X-CONJ"])
            lst8[11]=lst8[11]*max(0.0000000000000001,self.transition[".-CONJ"])
            self.scores[7]=(self.scores[7]*max(lst8))
            maxindex7=lst8.index(max(lst8))
            if(maxindex7==0):
                self.conj_string=self.parent.det_string+self.conj_string
            elif(maxindex7==1):
                self.conj_string=self.parent.adj_string+self.conj_string
            elif(maxindex7==2):
                self.conj_string=self.parent.adp_string+self.conj_string
            elif(maxindex7==3):
                self.conj_string=self.parent.adv_string+self.conj_string
            elif(maxindex7==4):
                self.conj_string=self.parent.noun_string+self.conj_string
            elif(maxindex7==5):
                self.conj_string=self.parent.num_string+self.conj_string
            elif(maxindex7==6):
                self.conj_string=self.parent.verb_string+self.conj_string
            elif(maxindex7==7):
                self.conj_string=self.parent.conj_string+self.conj_string
            elif(maxindex7==8):
                self.conj_string=self.parent.prt_string+self.conj_string
            elif(maxindex7==9):
                self.conj_string=self.parent.pron_string+self.conj_string
            elif(maxindex7==10):
                self.conj_string=self.parent.x_string+self.conj_string
            elif(maxindex7==11):
                self.conj_string=self.parent.dot_string+self.conj_string
            else:
                pass
            self.result_holder.append(self.conj_string)

            lst9=cpy_lst(self.parent.scores)
            lst9[0]=lst9[0]*max(0.0000000000000001,self.transition["DET-PRT"])
            lst9[1]=lst9[1]*max(0.0000000000000001,self.transition["ADJ-PRT"])
            lst9[2]=lst9[2]*max(0.0000000000000001,self.transition["ADP-PRT"])
            lst9[3]=lst9[3]*max(0.0000000000000001,self.transition["ADV-PRT"])
            lst9[4]=lst9[4]*max(0.0000000000000001,self.transition["NOUN-PRT"])
            lst9[5]=lst9[5]*max(0.0000000000000001,self.transition["NUM-PRT"])
            lst9[6]=lst9[6]*max(0.0000000000000001,self.transition["VERB-PRT"])
            lst9[7]=lst9[7]*max(0.0000000000000001,self.transition["CONJ-PRT"])
            lst9[8]=lst9[8]*max(0.0000000000000001,self.transition["PRT-PRT"])
            lst9[9]=lst9[9]*max(0.0000000000000001,self.transition["PRON-PRT"])
            lst9[10]=lst9[10]*max(0.0000000000000001,self.transition["X-PRT"])
            lst9[11]=lst9[11]*max(0.0000000000000001,self.transition[".-PRT"])
            self.scores[8]=(self.scores[8]*max(lst9))
            maxindex8=lst9.index(max(lst9))
            if(maxindex8==0):
                self.prt_string=self.parent.det_string+self.prt_string
            elif(maxindex8==1):
                self.prt_string=self.parent.adj_string+self.prt_string
            elif(maxindex8==2):
                self.prt_string=self.parent.adp_string+self.prt_string
            elif(maxindex8==3):
                self.prt_string=self.parent.adv_string+self.prt_string
            elif(maxindex8==4):
                self.prt_string=self.parent.noun_string+self.prt_string
            elif(maxindex8==5):
                self.prt_string=self.parent.num_string+self.prt_string
            elif(maxindex8==6):
                self.prt_string=self.parent.verb_string+self.prt_string
            elif(maxindex8==7):
                self.prt_string=self.parent.conj_string+self.prt_string
            elif(maxindex8==8):
                self.prt_string=self.parent.prt_string+self.prt_string
            elif(maxindex8==9):
                self.prt_string=self.parent.pron_string+self.prt_string
            elif(maxindex8==10):
                self.prt_string=self.parent.x_string+self.prt_string
            elif(maxindex8==11):
                self.prt_string=self.parent.dot_string+self.prt_string
            else:
                pass
            self.result_holder.append(self.prt_string)

            lst10=cpy_lst(self.parent.scores)
            lst10[0]=lst10[0]*max(0.0000000000000001,self.transition["DET-PRON"])
            lst10[1]=lst10[1]*max(0.0000000000000001,self.transition["ADJ-PRON"])
            lst10[2]=lst10[2]*max(0.0000000000000001,self.transition["ADP-PRON"])
            lst10[3]=lst10[3]*max(0.0000000000000001,self.transition["ADV-PRON"])
            lst10[4]=lst10[4]*max(0.0000000000000001,self.transition["NOUN-PRON"])
            lst10[5]=lst10[5]*max(0.0000000000000001,self.transition["NUM-PRON"])
            lst10[6]=lst10[6]*max(0.0000000000000001,self.transition["VERB-PRON"])
            lst10[7]=lst10[7]*max(0.0000000000000001,self.transition["CONJ-PRON"])
            lst10[8]=lst10[8]*max(0.0000000000000001,self.transition["PRT-PRON"])
            lst10[9]=lst10[9]*max(0.0000000000000001,self.transition["PRON-PRON"])
            lst10[10]=lst10[10]*max(0.0000000000000001,self.transition["X-PRON"])
            lst10[11]=lst10[11]*max(0.0000000000000001,self.transition[".-PRON"])
            self.scores[9]=(self.scores[9]*max(lst10))
            maxindex9=lst10.index(max(lst10))
            if(maxindex9==0):
                self.pron_string=self.parent.det_string+self.pron_string
            elif(maxindex9==1):
                self.pron_string=self.parent.adj_string+self.pron_string
            elif(maxindex9==2):
                self.pron_string=self.parent.adp_string+self.pron_string
            elif(maxindex9==3):
                self.pron_string=self.parent.adv_string+self.pron_string
            elif(maxindex9==4):
                self.pron_string=self.parent.noun_string+self.pron_string
            elif(maxindex9==5):
                self.pron_string=self.parent.num_string+self.pron_string
            elif(maxindex9==6):
                self.pron_string=self.parent.verb_string+self.pron_string
            elif(maxindex9==7):
                self.pron_string=self.parent.conj_string+self.pron_string
            elif(maxindex9==8):
                self.pron_string=self.parent.prt_string+self.pron_string
            elif(maxindex9==9):
                self.pron_string=self.parent.pron_string+self.pron_string
            elif(maxindex9==10):
                self.pron_string=self.parent.x_string+self.pron_string
            elif(maxindex9==11):
                self.pron_string=self.parent.dot_string+self.pron_string
            else:
                pass
            self.result_holder.append(self.pron_string)

            lst11=cpy_lst(self.parent.scores)
            lst11[0]=lst11[0]*max(0.0000000000000001,self.transition["DET-X"])
            lst11[1]=lst11[1]*max(0.0000000000000001,self.transition["ADJ-X"])
            lst11[2]=lst11[2]*max(0.0000000000000001,self.transition["ADP-X"])
            lst11[3]=lst11[3]*max(0.0000000000000001,self.transition["ADV-X"])
            lst11[4]=lst11[4]*max(0.0000000000000001,self.transition["NOUN-X"])
            lst11[5]=lst11[5]*max(0.0000000000000001,self.transition["NUM-X"])
            lst11[6]=lst11[6]*max(0.0000000000000001,self.transition["VERB-X"])
            lst11[7]=lst11[7]*max(0.0000000000000001,self.transition["CONJ-X"])
            lst11[8]=lst11[8]*max(0.0000000000000001,self.transition["PRT-X"])
            lst11[9]=lst11[9]*max(0.0000000000000001,self.transition["PRON-X"])
            lst11[10]=lst11[10]*max(0.0000000000000001,self.transition["X-X"])
            lst11[11]=lst11[11]*max(0.0000000000000001,self.transition[".-X"])
            self.scores[10]=(self.scores[10]*max(lst11))
            maxindex10=lst11.index(max(lst11))
            if(maxindex10==0):
                self.x_string=self.parent.det_string+self.x_string
            elif(maxindex10==1):
                self.x_string=self.parent.adj_string+self.x_string
            elif(maxindex10==2):
                self.x_string=self.parent.adp_string+self.x_string
            elif(maxindex10==3):
                self.x_string=self.parent.adv_string+self.x_string
            elif(maxindex10==4):
                self.x_string=self.parent.noun_string+self.x_string
            elif(maxindex10==5):
                self.x_string=self.parent.num_string+self.x_string
            elif(maxindex10==6):
                self.x_string=self.parent.verb_string+self.x_string
            elif(maxindex10==7):
                self.x_string=self.parent.conj_string+self.x_string
            elif(maxindex10==8):
                self.x_string=self.parent.prt_string+self.x_string
            elif(maxindex10==9):
                self.x_string=self.parent.pron_string+self.x_string
            elif(maxindex10==10):
                self.x_string=self.parent.x_string+self.x_string
            elif(maxindex10==11):
                self.x_string=self.parent.dot_string+self.x_string
            else:
                pass
            self.result_holder.append(self.x_string)

            lst12=cpy_lst(self.parent.scores)
            lst12[0]=lst12[0]*max(0.0000000000000001,self.transition["DET-."])
            lst12[1]=lst12[1]*max(0.0000000000000001,self.transition["ADJ-."])
            lst12[2]=lst12[2]*max(0.0000000000000001,self.transition["ADP-."])
            lst12[3]=lst12[3]*max(0.0000000000000001,self.transition["ADV-."])
            lst12[4]=lst12[4]*max(0.0000000000000001,self.transition["NOUN-."])
            lst12[5]=lst12[5]*max(0.0000000000000001,self.transition["NUM-."])
            lst12[6]=lst12[6]*max(0.0000000000000001,self.transition["VERB-."])
            lst12[7]=lst12[7]*max(0.0000000000000001,self.transition["CONJ-."])
            lst12[8]=lst12[8]*max(0.0000000000000001,self.transition["PRT-."])
            lst12[9]=lst12[9]*max(0.0000000000000001,self.transition["PRON-."])
            lst12[10]=lst12[10]*max(0.0000000000000001,self.transition["X-."])
            lst12[11]=lst12[11]*max(0.0000000000000001,self.transition[".-."])
            self.scores[11]=(self.scores[11]*max(lst12))
            maxindex11=lst12.index(max(lst12))
            if(maxindex11==0):
                self.dot_string=self.parent.det_string+self.dot_string
            elif(maxindex11==1):
                self.dot_string=self.parent.adj_string+self.dot_string
            elif(maxindex11==2):
                self.dot_string=self.parent.adp_string+self.dot_string
            elif(maxindex11==3):
                self.dot_string=self.parent.adv_string+self.dot_string
            elif(maxindex11==4):
                self.dot_string=self.parent.noun_string+self.dot_string
            elif(maxindex11==5):
                self.dot_string=self.parent.num_string+self.dot_string
            elif(maxindex11==6):
                self.dot_string=self.parent.verb_string+self.dot_string
            elif(maxindex11==7):
                self.dot_string=self.parent.conj_string+self.dot_string
            elif(maxindex11==8):
                self.dot_string=self.parent.prt_string+self.dot_string
            elif(maxindex11==9):
                self.dot_string=self.parent.pron_string+self.dot_string
            elif(maxindex11==10):
                self.dot_string=self.parent.x_string+self.dot_string
            elif(maxindex11==11):
                self.dot_string=self.parent.dot_string+self.dot_string
            else:
                pass
            self.result_holder.append(self.dot_string)



            self.maxi=self.scores.index(max(self.scores))



            

    def ret_maxi_string(self):
        #return self.result_holder[self.maxi]
        #print(self.maxi)
        return self.result_holder[self.maxi]

        


def max_pro(lst,w):
    result=[]
    result_pos=""
    for i in lst:
        if(w in i):
            result.append(i[w])
        else:
            result.append(0.000000000000000000000001)
    
    max_index=result.index(max(result))
    if(max_index==0):
        result_pos="det"
    elif(max_index==1):
        result_pos="adj"
    elif(max_index==2):
        result_pos="adp"
    elif(max_index==3):
        result_pos="adv"
    elif(max_index==4):
        result_pos="noun"
    elif(max_index==5):
        result_pos="num"
    elif(max_index==6):
        result_pos="verb"
    elif(max_index==7):
        result_pos="conj"
    elif(max_index==8):
        result_pos="prt"
    elif(max_index==9):
        result_pos="pron"
    elif(max_index==10):
        result_pos="x"
    elif(max_index==11):
        result_pos="."
    else:
        pass
    return result_pos

class Solver:
    # Calculate the log of the posterior probability of a given sentence
    #  with a given part-of-speech labeling. Right now just returns -999 -- fix this!
    def __init__(self):
    	self.initial_prob={}
    	self.prob_trans={}
        
    	self.det_set={}
    	self.adv_set={}
    	self.adj_set={}
    	self.adp_set={}
    	self.conj_set={}
    	self.noun_set={}
    	self.num_set={}
    	self.pron_set={}
    	self.prt_set={}
    	self.verb_set={}
    	self.x_set={}
    	self.dot_set={}


    	self.pos_pro={"DET":0.0,"ADJ":0.0,"ADV":0.0,"ADP":0.0,"CONJ":0.0,"NOUN":0.0,"NUM":0.0,"PRON":0.0,"PRT":0.0,"VERB":0.0,"X":0.0,".":0.0}


    def posterior(self, model, sentence, label):
        if model == "Simple":
            prob=0
            for i in range(len(sentence)):
                if(label[i]=="det"):
                    if(sentence[i] in self.det_set):
                        prob=prob+math.log(self.det_set[sentence[i]])+math.log(self.pos_pro["DET"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["DET"])
                elif(label[i]=="adj"):
                    if(sentence[i] in self.adj_set):
                        prob=prob+math.log(self.adj_set[sentence[i]])+math.log(self.pos_pro["ADJ"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["ADJ"])
                elif(label[i]=="adv"):
                    if(sentence[i] in self.adv_set):
                        prob=prob+math.log(self.adv_set[sentence[i]])+math.log(self.pos_pro["ADV"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["ADV"])
                elif(label[i]=="adp"):
                    if(sentence[i] in self.adp_set):
                        prob=prob+math.log(self.adp_set[sentence[i]])+math.log(self.pos_pro["ADP"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["ADP"])
                elif(label[i]=="conj"):
                    if(sentence[i] in self.conj_set):
                        prob=prob+math.log(self.conj_set[sentence[i]])+math.log(self.pos_pro["CONJ"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["CONJ"])
                elif(label[i]=="noun"):
                    if(sentence[i] in self.noun_set):
                        prob=prob+math.log(self.noun_set[sentence[i]])+math.log(self.pos_pro["NOUN"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["NOUN"])
                elif(label[i]=="num"):
                    if(sentence[i] in self.num_set):
                        prob=prob+math.log(self.num_set[sentence[i]])+math.log(self.pos_pro["NUM"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["NUM"])
                elif(label[i]=="pron"):
                    if(sentence[i] in self.pron_set):
                        prob=prob+math.log(self.pron_set[sentence[i]])+math.log(self.pos_pro["PRON"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["PRON"])
                elif(label[i]=="prt"):
                    if(sentence[i] in self.prt_set):
                        prob=prob+math.log(self.prt_set[sentence[i]])+math.log(self.pos_pro["PRT"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["PRT"])
                elif(label[i]=="verb"):
                    if(sentence[i] in self.verb_set):
                        prob=prob+math.log(self.verb_set[sentence[i]])+math.log(self.pos_pro["VERB"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["VERB"])
                elif(label[i]=="x"):
                    if(sentence[i] in self.x_set):
                        prob=prob+math.log(self.x_set[sentence[i]])+math.log(self.pos_pro["X"])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["X"])
                elif(label[i]=="."):
                    if(sentence[i] in self.dot_set):
                        prob=prob+math.log(self.dot_set[sentence[i]])+math.log(self.pos_pro["."])
                    else:
                        prob=prob+math.log(0.000000000000000001)+math.log(self.pos_pro["."])

            return prob


        elif model == "HMM":
            prob=0
            for i in range(len(sentence)):
                if(i==0):
                    if(label[i]=="det"):
                        if(sentence[i] in self.det_set):
                            prob=prob+math.log(self.det_set[sentence[i]])+math.log(self.initial_prob["DET"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["DET"])
                    elif(label[i]=="adj"):
                        if(sentence[i] in self.adj_set):
                            prob=prob+math.log(self.adj_set[sentence[i]])+math.log(self.initial_prob["ADJ"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["ADJ"])
                    elif(label[i]=="adv"):
                        if(sentence[i] in self.adv_set):
                            prob=prob+math.log(self.adv_set[sentence[i]])+math.log(self.initial_prob["ADV"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["ADV"])
                    elif(label[i]=="adp"):
                        if(sentence[i] in self.adp_set):
                            prob=prob+math.log(self.adp_set[sentence[i]])+math.log(self.initial_prob["ADP"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["ADP"])
                    elif(label[i]=="conj"):
                        if(sentence[i] in self.conj_set):
                            prob=prob+math.log(self.conj_set[sentence[i]])+math.log(self.initial_prob["CONJ"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["CONJ"])
                    elif(label[i]=="noun"):
                        if(sentence[i] in self.noun_set):
                            prob=prob+math.log(self.noun_set[sentence[i]])+math.log(self.initial_prob["NOUN"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["NOUN"])
                    elif(label[i]=="num"):
                        if(sentence[i] in self.num_set):
                            prob=prob+math.log(self.num_set[sentence[i]])+math.log(self.initial_prob["NUM"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["NUM"])
                    elif(label[i]=="pron"):
                        if(sentence[i] in self.pron_set):
                            prob=prob+math.log(self.pron_set[sentence[i]])+math.log(self.initial_prob["PRON"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["PRON"])
                    elif(label[i]=="prt"):
                        if(sentence[i] in self.prt_set):
                            prob=prob+math.log(self.prt_set[sentence[i]])+math.log(self.initial_prob["PRT"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["PRT"])
                    elif(label[i]=="verb"):
                        if(sentence[i] in self.verb_set):
                            prob=prob+math.log(self.verb_set[sentence[i]])+math.log(self.initial_prob["VERB"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["VERB"])
                    elif(label[i]=="x"):
                        if(sentence[i] in self.x_set):
                            prob=prob+math.log(self.x_set[sentence[i]])+math.log(self.initial_prob["X"])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["X"])
                    elif(label[i]=="."):
                        if(sentence[i] in self.dot_set):
                            prob=prob+math.log(self.dot_set[sentence[i]])+math.log(self.initial_prob["."])
                        else:
                            prob=prob+math.log(0.000000000000000001)+math.log(self.initial_prob["."])
                else:
                    edge1=label[i-1]+"-"+label[i]
                    edge=edge1.upper()
                    if(self.prob_trans[edge]>0):
                        if(label[i]=="det"):
                            if(sentence[i] in self.det_set):
                                prob=prob+math.log(self.det_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="adj"):
                            if(sentence[i] in self.adj_set):
                                prob=prob+math.log(self.adj_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="adv"):
                            if(sentence[i] in self.adv_set):
                                prob=prob+math.log(self.adv_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="adp"):
                            if(sentence[i] in self.adp_set):
                                prob=prob+math.log(self.adp_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="conj"):
                            if(sentence[i] in self.conj_set):
                                prob=prob+math.log(self.conj_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="noun"):
                            if(sentence[i] in self.noun_set):
                                prob=prob+math.log(self.noun_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="num"):
                            if(sentence[i] in self.num_set):
                                prob=prob+math.log(self.num_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="pron"):
                            if(sentence[i] in self.pron_set):
                                prob=prob+math.log(self.pron_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="prt"):
                            if(sentence[i] in self.prt_set):
                                prob=prob+math.log(self.prt_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="verb"):
                            if(sentence[i] in self.verb_set):
                                prob=prob+math.log(self.verb_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="x"):
                            if(sentence[i] in self.x_set):
                                prob=prob+math.log(self.x_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                        elif(label[i]=="."):
                            if(sentence[i] in self.dot_set):
                                prob=prob+math.log(self.dot_set[sentence[i]])+math.log(self.prob_trans[edge])
                            else:
                                prob=prob+math.log(0.000000000000000001)+math.log(self.prob_trans[edge])
                    else:
                        prob=prob+math.log(self.ret_dict(label[i],sentence[i]))+math.log(0.000000000000000001)

            return prob



        elif model == "Complex":
            prob=0
            for i in range(len(sentence)):
                if(len(sentence)==1):
                    prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.initial_prob[label[i].upper()]))
                elif(i==0):
                    edge1=label[i]+"-"+label[i+1]
                    edge=edge1.upper()
                    if(self.prob_trans[edge]>0):
                        prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.initial_prob[label[i].upper()]))+(math.log(self.prob_trans[edge]))
                    else:
                        prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.initial_prob[label[i].upper()]))+(math.log(0.0000000000000001))
                elif(i==len(sentence)-1):
                    edge1=label[i-1]+"-"+label[0]
                    edge2=label[i]+"-"+label[i-1]
                    edge=edge1.upper()
                    edge2u=edge2.upper()
                    if(self.prob_trans[edge]>0 and self.prob_trans[edge2u]>0):
                        prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.ret_dict(label[i-1],sentence[i])))+(math.log(self.prob_trans[edge]))+(math.log(self.prob_trans[edge2u]))
                    elif(self.prob_trans[edge]>0 and self.prob_trans[edge2u]<=0):
                        prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.ret_dict(label[i-1],sentence[i])))+(math.log(self.prob_trans[edge]))+(math.log(0.0000000000000001))
                    elif(self.prob_trans[edge]<=0 and self.prob_trans[edge2u]>0):
                        prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.ret_dict(label[i-1],sentence[i])))+(math.log(0.00000000000000001))+(math.log(self.prob_trans[edge2u]))
                    else:
                        prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.ret_dict(label[i-1],sentence[i])))+(math.log(0.00000000000000001))+(math.log(0.00000000000000001))
                else:
                    edge1=label[i]+"-"+label[i+1]
                    edge2=label[i-1]+"-"+label[i]
                    edge=edge1.upper()
                    edge2u=edge2.upper()
                    if(self.prob_trans[edge]>0 and self.prob_trans[edge2u]>0):
                        prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.ret_dict(label[i-1],sentence[i-1])))+(math.log(self.ret_dict(label[i-1],sentence[i])))+(math.log(self.ret_dict(label[i],sentence[i+1])))+(math.log(self.ret_dict(label[i+1],sentence[i+1])))+(math.log(self.prob_trans[edge]))+(math.log(self.prob_trans[edge2u]))
                    elif(self.prob_trans[edge]>0 and self.prob_trans[edge2u]<=0):
                        prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.ret_dict(label[i-1],sentence[i-1])))+(math.log(self.ret_dict(label[i-1],sentence[i])))+(math.log(self.ret_dict(label[i],sentence[i+1])))+(math.log(self.ret_dict(label[i+1],sentence[i+1])))+(math.log(self.prob_trans[edge]))+(math.log(0.0000000000000001))
                    elif(self.prob_trans[edge]<=0 and self.prob_trans[edge2u]>0):
                        prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.ret_dict(label[i-1],sentence[i-1])))+(math.log(self.ret_dict(label[i-1],sentence[i])))+(math.log(self.ret_dict(label[i],sentence[i+1])))+(math.log(self.ret_dict(label[i+1],sentence[i+1])))+(math.log(0.0000000000000001))+(math.log(self.prob_trans[edge2u]))
                    else:
                        prob+=(math.log(self.ret_dict(label[i],sentence[i])))+(math.log(self.ret_dict(label[i-1],sentence[i-1])))+(math.log(self.ret_dict(label[i-1],sentence[i])))+(math.log(self.ret_dict(label[i],sentence[i+1])))+(math.log(self.ret_dict(label[i+1],sentence[i+1])))+(math.log(0.0000000000000001))+(math.log(0.0000000000000001))
            prob=prob/10
            return prob


        else:
            print("Unknown algo!")

    # Do the training!
    #
    def train(self, data):
        tags_start={"DET":0.0,"ADJ":0.0,"ADV":0.0,"ADP":0.0,"CONJ":0.0,"NOUN":0.0,"NUM":0.0,"PRON":0.0,"PRT":0.0,"VERB":0.0,"X":0.0,".":0.0}
        c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12=1,1,1,1,1,1,1,1,1,1,1,1
        for i in range(len(data)):
        	if(data[i][1][0]=="DET" or data[i][1][0]=="det"):
        		c1+=1
        	elif(data[i][1][0]=="ADJ" or data[i][1][0]=="adj"):
        		c2+=1
        	elif(data[i][1][0]=="ADV" or data[i][1][0]=="adv"):
        		c3+=1
        	elif(data[i][1][0]=="ADP" or data[i][1][0]=="adp"):
        		c4+=1
        	elif(data[i][1][0]=="CONJ" or data[i][1][0]=="conj"):
        		c5+=1
        	elif(data[i][1][0]=="NOUN" or data[i][1][0]=="noun"):
        		c6+=1
        	elif(data[i][1][0]=="NUM" or data[i][1][0]=="num"):
        		c7+=1
        	elif(data[i][1][0]=="PRON" or data[i][1][0]=="pron"):
        		c8+=1
        	elif(data[i][1][0]=="PRT" or data[i][1][0]=="prt"):
        		c9+=1
        	elif(data[i][1][0]=="VERB" or data[i][1][0]=="verb"):
        		c10+=1
        	elif(data[i][1][0]=="X" or data[i][1][0]=="x"):
        		c11+=1
        	elif(data[i][1][0]=="."):
        		c12+=1
        	else:
        		pass
        tags_start["DET"]=c1/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["ADJ"]=c2/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["ADV"]=c3/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["ADP"]=c4/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["CONJ"]=c5/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["NOUN"]=c6/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["NUM"]=c7/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["PRON"]=c8/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["PRT"]=c9/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["VERB"]=c10/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["X"]=c11/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        tags_start["."]=c12/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
       	self.initial_prob=tags_start

        
        c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12=1,1,1,1,1,1,1,1,1,1,1,1
        for i in range(len(data)):
            for j in range(len(data[i][1])):
                if(data[i][1][j]=="DET" or data[i][1][j]=="det"):
                    c1+=1
                elif(data[i][1][j]=="ADJ" or data[i][1][j]=="adj"):
                    c2+=1
                elif(data[i][1][j]=="ADV" or data[i][1][j]=="adv"):
                    c3+=1
                elif(data[i][1][j]=="ADP" or data[i][1][j]=="adp"):
                    c4+=1
                elif(data[i][1][j]=="CONJ" or data[i][1][j]=="conj"):
                    c5+=1
                elif(data[i][1][j]=="NOUN" or data[i][1][j]=="noun"):
                    c6+=1
                elif(data[i][1][j]=="NUM" or data[i][1][j]=="num"):
                    c7+=1
                elif(data[i][1][j]=="PRON" or data[i][1][j]=="pron"):
                    c8+=1
                elif(data[i][1][j]=="PRT" or data[i][1][j]=="prt"):
                    c9+=1
                elif(data[i][1][j]=="VERB" or data[i][1][j]=="verb"):
                    c10+=1
                elif(data[i][1][j]=="X" or data[i][1][j]=="x"):
                    c11+=1
                elif(data[i][1][j]=="."):
                    c12+=1
                else:
                    pass
        self.pos_pro["DET"]=c1/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["ADJ"]=c2/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["ADV"]=c3/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["ADP"]=c4/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["CONJ"]=c5/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["NOUN"]=c6/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["NUM"]=c7/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["PRON"]=c8/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["PRT"]=c9/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["VERB"]=c10/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["X"]=c11/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        self.pos_pro["."]=c12/(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12)
        #print(self.pos_pro)
       

        transition_prob={"DET-DET":1,"DET-ADJ":1,"DET-ADV":1,"DET-ADP":1,"DET-CONJ":1,"DET-NOUN":1,"DET-NUM":1,"DET-PRON":1,"DET-PRT":1,"DET-VERB":1,"DET-X":1,"DET-.":1,"ADJ-DET":1,"ADJ-ADJ":1,"ADJ-ADV":1,"ADJ-ADP":1,"ADJ-CONJ":1,"ADJ-NOUN":1,"ADJ-NUM":1,"ADJ-PRON":1,"ADJ-PRT":1,"ADJ-VERB":1,"ADJ-X":1,"ADJ-.":1,"ADV-DET":1,"ADV-ADJ":1,"ADV-ADV":1,"ADV-ADP":1,"ADV-CONJ":1,"ADV-NOUN":1,"ADV-NUM":1,"ADV-PRON":1,"ADV-PRT":1,"ADV-VERB":1,"ADV-X":1,"ADV-.":1,"ADP-DET":1,"ADP-ADJ":1,"ADP-ADV":1,"ADP-ADP":1,"ADP-CONJ":1,"ADP-NOUN":1,"ADP-NUM":1,"ADP-PRON":1,"ADP-PRT":1,"ADP-VERB":1,"ADP-X":1,"ADP-.":1,"CONJ-DET":1,"CONJ-ADJ":1,"CONJ-ADV":1,"CONJ-ADP":1,"CONJ-CONJ":1,"CONJ-NOUN":1,"CONJ-NUM":1,"CONJ-PRON":1,"CONJ-PRT":1,"CONJ-VERB":1,"CONJ-X":1,"CONJ-.":1,"NOUN-DET":1,"NOUN-ADJ":1,"NOUN-ADV":1,"NOUN-ADP":1,"NOUN-CONJ":1,"NOUN-NOUN":1,"NOUN-NUM":1,"NOUN-PRON":1,"NOUN-PRT":1,"NOUN-VERB":1,"NOUN-X":1,"NOUN-.":1,"NUM-DET":1,"NUM-ADJ":1,"NUM-ADV":1,"NUM-ADP":1,"NUM-CONJ":1,"NUM-NOUN":1,"NUM-NUM":1,"NUM-PRON":1,"NUM-PRT":1,"NUM-VERB":1,"NUM-X":1,"NUM-.":1,"PRON-DET":1,"PRON-ADJ":1,"PRON-ADV":1,"PRON-ADP":1,"PRON-CONJ":1,"PRON-NOUN":1,"PRON-NUM":1,"PRON-PRON":1,"PRON-PRT":1,"PRON-VERB":1,"PRON-X":1,"PRON-.":1,"PRT-DET":1,"PRT-ADJ":1,"PRT-ADV":1,"PRT-ADP":1,"PRT-CONJ":1,"PRT-NOUN":1,"PRT-NUM":1,"PRT-PRON":1,"PRT-PRT":1,"PRT-VERB":1,"PRT-X":1,"PRT-.":1,"VERB-DET":1,"VERB-ADJ":1,"VERB-ADV":1,"VERB-ADP":1,"VERB-CONJ":1,"VERB-NOUN":1,"VERB-NUM":1,"VERB-PRON":1,"VERB-PRT":1,"VERB-VERB":1,"VERB-X":1,"VERB-.":1,"X-DET":1,"X-ADJ":1,"X-ADV":1,"X-ADP":1,"X-CONJ":1,"X-NOUN":1,"X-NUM":1,"X-PRON":1,"X-PRT":1,"X-VERB":1,"X-X":1,"X-.":1,".-DET":1,".-ADJ":1,".-ADV":1,".-ADP":1,".-CONJ":1,".-NOUN":1,".-NUM":1,".-PRON":1,".-PRT":1,".-VERB":1,".-X":1,".-.":1}
        list_trans_prob=[1 for i in range(144)]
        for i in range(len(data)):
        	for j in range(len(data[i][1])):
        		if(data[i][1][j]=="DET" or data[i][1][j]=="det"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[0]=list_trans_prob[0]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[1]=list_trans_prob[1]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[2]=list_trans_prob[2]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[3]=list_trans_prob[3]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[4]=list_trans_prob[4]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[5]=list_trans_prob[5]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[6]=list_trans_prob[6]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[7]=list_trans_prob[7]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[8]=list_trans_prob[8]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[9]=list_trans_prob[9]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[10]=list_trans_prob[10]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[11]=list_trans_prob[11]+1
        			else:
        				pass

        		elif(data[i][1][j]=="ADJ" or data[i][1][j]=="adj"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[12]=list_trans_prob[12]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[13]=list_trans_prob[13]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[14]=list_trans_prob[14]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[15]=list_trans_prob[15]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[16]=list_trans_prob[16]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[17]=list_trans_prob[17]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[18]=list_trans_prob[18]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[19]=list_trans_prob[19]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[20]=list_trans_prob[20]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[21]=list_trans_prob[21]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[22]=list_trans_prob[22]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[23]=list_trans_prob[23]+1
        			else:
        				pass

        		elif(data[i][1][j]=="adv" or data[i][1][j]=="adv"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[24]=list_trans_prob[24]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[25]=list_trans_prob[25]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[26]=list_trans_prob[26]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[27]=list_trans_prob[27]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[28]=list_trans_prob[28]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[29]=list_trans_prob[29]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[30]=list_trans_prob[30]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[31]=list_trans_prob[31]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[32]=list_trans_prob[32]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[33]=list_trans_prob[33]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[34]=list_trans_prob[34]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[35]=list_trans_prob[35]+1
        			else:
        				pass

        		elif(data[i][1][j]=="ADP" or data[i][1][j]=="adp"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[36]=list_trans_prob[36]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[37]=list_trans_prob[37]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[38]=list_trans_prob[38]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[39]=list_trans_prob[39]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[40]=list_trans_prob[40]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[41]=list_trans_prob[41]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[42]=list_trans_prob[42]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[43]=list_trans_prob[43]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[44]=list_trans_prob[44]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[45]=list_trans_prob[45]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[46]=list_trans_prob[46]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[47]=list_trans_prob[47]+1
        			else:
        				pass

        		elif(data[i][1][j]=="CONJ" or data[i][1][j]=="conj"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[48]=list_trans_prob[48]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[49]=list_trans_prob[49]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[50]=list_trans_prob[50]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[51]=list_trans_prob[51]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[52]=list_trans_prob[52]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[53]=list_trans_prob[53]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[54]=list_trans_prob[54]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[55]=list_trans_prob[55]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[56]=list_trans_prob[56]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[57]=list_trans_prob[57]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[58]=list_trans_prob[58]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[59]=list_trans_prob[59]+1
        			else:
        				pass

        		elif(data[i][1][j]=="NOUN" or data[i][1][j]=="noun"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[60]=list_trans_prob[60]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[61]=list_trans_prob[61]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[62]=list_trans_prob[62]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[63]=list_trans_prob[63]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[64]=list_trans_prob[64]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[65]=list_trans_prob[65]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[66]=list_trans_prob[66]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[67]=list_trans_prob[67]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[68]=list_trans_prob[68]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[69]=list_trans_prob[69]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[70]=list_trans_prob[70]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[71]=list_trans_prob[71]+1
        			else:
        				pass

        		elif(data[i][1][j]=="NUM" or data[i][1][j]=="num"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[72]=list_trans_prob[72]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[73]=list_trans_prob[73]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[74]=list_trans_prob[74]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[75]=list_trans_prob[75]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[76]=list_trans_prob[76]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[77]=list_trans_prob[77]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[78]=list_trans_prob[78]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[79]=list_trans_prob[79]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[80]=list_trans_prob[80]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[81]=list_trans_prob[81]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[82]=list_trans_prob[82]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[83]=list_trans_prob[83]+1
        			else:
        				pass

        		elif(data[i][1][j]=="PRON" or data[i][1][j]=="pron"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[84]=list_trans_prob[84]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[85]=list_trans_prob[85]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[86]=list_trans_prob[86]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[87]=list_trans_prob[87]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[88]=list_trans_prob[88]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[89]=list_trans_prob[89]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[90]=list_trans_prob[90]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[91]=list_trans_prob[91]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[92]=list_trans_prob[92]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[93]=list_trans_prob[93]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[94]=list_trans_prob[94]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[95]=list_trans_prob[95]+1
        			else:
        				pass

        		elif(data[i][1][j]=="PRT" or data[i][1][j]=="prt"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[96]=list_trans_prob[96]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[97]=list_trans_prob[97]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[98]=list_trans_prob[98]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[99]=list_trans_prob[99]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[100]=list_trans_prob[100]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[101]=list_trans_prob[101]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[102]=list_trans_prob[102]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[103]=list_trans_prob[103]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[104]=list_trans_prob[104]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[105]=list_trans_prob[105]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[106]=list_trans_prob[106]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[107]=list_trans_prob[107]+1
        			else:
        				pass

        		elif(data[i][1][j]=="VERB" or data[i][1][j]=="verb"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[108]=list_trans_prob[108]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[109]=list_trans_prob[109]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[110]=list_trans_prob[110]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[111]=list_trans_prob[111]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[112]=list_trans_prob[112]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[113]=list_trans_prob[113]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[114]=list_trans_prob[114]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[115]=list_trans_prob[115]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[116]=list_trans_prob[116]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[117]=list_trans_prob[117]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[118]=list_trans_prob[118]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[119]=list_trans_prob[119]+1
        			else:
        				pass

        		if(data[i][1][j]=="X" or data[i][1][j]=="x"):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[120]=list_trans_prob[120]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[121]=list_trans_prob[121]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[122]=list_trans_prob[122]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[123]=list_trans_prob[123]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[124]=list_trans_prob[124]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[125]=list_trans_prob[125]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[126]=list_trans_prob[126]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[127]=list_trans_prob[127]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[128]=list_trans_prob[128]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[129]=list_trans_prob[129]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[130]=list_trans_prob[130]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[131]=list_trans_prob[131]+1
        			else:
        				pass

        		if(data[i][1][j]=="."):
        			if(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="det") or (data[i][1][j+1]=="DET"))):
        				list_trans_prob[132]=list_trans_prob[132]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adj") or (data[i][1][j+1]=="ADJ"))):
        				list_trans_prob[133]=list_trans_prob[133]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adv") or (data[i][1][j+1]=="ADV"))):
        				list_trans_prob[134]=list_trans_prob[134]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="adp") or (data[i][1][j+1]=="ADP"))):
        				list_trans_prob[135]=list_trans_prob[135]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="conj") or (data[i][1][j+1]=="CONJ"))):
        				list_trans_prob[136]=list_trans_prob[136]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="noun") or (data[i][1][j+1]=="NOUN"))):
        				list_trans_prob[137]=list_trans_prob[137]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="num") or (data[i][1][j+1]=="NUM"))):
        				list_trans_prob[138]=list_trans_prob[138]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="pron") or (data[i][1][j+1]=="PRON"))):
        				list_trans_prob[139]=list_trans_prob[139]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="prt") or (data[i][1][j+1]=="PRT"))):
        				list_trans_prob[140]=list_trans_prob[140]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="verb") or (data[i][1][j+1]=="VERB"))):
        				list_trans_prob[141]=list_trans_prob[141]+1
        			elif(((j+1)<len(data[i][1])) and ((data[i][1][j+1]=="X") or (data[i][1][j+1]=="x"))):
        				list_trans_prob[142]=list_trans_prob[142]+1
        			elif(((j+1)<len(data[i][1])) and (data[i][1][j+1]==".")):
        				list_trans_prob[143]=list_trans_prob[143]+1
        			else:
        				pass

        		else:
        			pass
        
        keys_list_object=transition_prob.keys()
        keys_list=list(keys_list_object)
        sum_trans_prob=0
        for i in list_trans_prob:
        	sum_trans_prob=sum_trans_prob+i
        for i in range(len(list_trans_prob)):
        	list_trans_prob[i]=(list_trans_prob[i]/sum_trans_prob)
        for i in range(len(keys_list)):
        	transition_prob[keys_list[i]]=list_trans_prob[i]

        self.prob_trans=transition_prob
        
        set_det=set()
        set_adv=set()
        set_adj=set()
        set_adp=set()
        set_noun=set()
        set_num=set()
        set_verb=set()
        set_conj=set()
        set_prt=set()
        set_x=set()
        set_pron=set()
        set_dot=set()
        for i in range(len(data)):
        	for j in range(len(data[i][0])):
        		if(data[i][1][j]=="det" or data[i][1][j]=="DET"):
        			set_det.add(data[i][0][j])
        		elif(data[i][1][j]=="adv" or data[i][1][j]=="ADV"):
        			set_adv.add(data[i][0][j])
        		elif(data[i][1][j]=="adj" or data[i][1][j]=="ADJ"):
        			set_adj.add(data[i][0][j])
        		elif(data[i][1][j]=="adp" or data[i][1][j]=="ADP"):
        			set_adp.add(data[i][0][j])
        		elif(data[i][1][j]=="NOUN" or data[i][1][j]=="noun"):
        			set_noun.add(data[i][0][j])
        		elif(data[i][1][j]=="num" or data[i][1][j]=="NUM"):
        			set_num.add(data[i][0][j])
        		elif(data[i][1][j]=="VERB" or data[i][1][j]=="verb"):
        			set_verb.add(data[i][0][j])
        		elif(data[i][1][j]=="CONJ" or data[i][1][j]=="conj"):
        			set_conj.add(data[i][0][j])
        		elif(data[i][1][j]=="PRT" or data[i][1][j]=="prt"):
        			set_prt.add(data[i][0][j])
        		elif(data[i][1][j]=="x" or data[i][1][j]=="X"):
        			set_x.add(data[i][0][j])
        		elif(data[i][1][j]=="PRON" or data[i][1][j]=="pron"):
        			set_pron.add(data[i][0][j])
        		elif(data[i][1][j]=="."):
        			set_dot.add(data[i][0][j])
        		else:
        			pass

        #print(set_det)
        #Calculation for Emission Prob DET
        for i in set_det:
        	self.det_set[i]=0
        
        for i in set_adj:
            self.adj_set[i]=0
        
        for i in set_adv:
            self.adv_set[i]=0

        for i in set_adp:
            self.adp_set[i]=0

        for i in set_noun:
            self.noun_set[i]=0

        for i in set_num:
            self.num_set[i]=0

        for i in set_verb:
            self.verb_set[i]=0

        for i in set_conj:
            self.conj_set[i]=0

        for i in set_prt:
            self.prt_set[i]=0

        for i in set_pron:
            self.pron_set[i]=0

        for i in set_x:
            self.x_set[i]=0

        for i in set_dot:
            self.dot_set[i]=0


        for i in range(len(data)):
        	for j in range(len(data[i][0])):
                    if((data[i][1][j]=="DET") or (data[i][1][j]=="det")):
                        self.det_set[data[i][0][j]]=self.det_set[data[i][0][j]]+1
                    elif((data[i][1][j]=="ADJ") or (data[i][1][j]=="adj")):
                        self.adj_set[data[i][0][j]]=self.adj_set[data[i][0][j]]+1
                    elif((data[i][1][j]=="ADP") or (data[i][1][j]=="adp")):
                        self.adp_set[data[i][0][j]]=self.adp_set[data[i][0][j]]+1
                    elif((data[i][1][j]=="NOUN") or (data[i][1][j]=="noun")):
                        self.noun_set[data[i][0][j]]=self.noun_set[data[i][0][j]]+1
                    elif((data[i][1][j]=="NUM") or (data[i][1][j]=="num")):
                        self.num_set[data[i][0][j]]=self.num_set[data[i][0][j]]+1
                    elif((data[i][1][j]=="VERB") or (data[i][1][j]=="verb")):
                        self.verb_set[data[i][0][j]]=self.verb_set[data[i][0][j]]+1
                    elif((data[i][1][j]=="ADV") or (data[i][1][j]=="adv")):
                        self.adv_set[data[i][0][j]]=self.adv_set[data[i][0][j]]+1
                    elif((data[i][1][j]=="CONJ") or (data[i][1][j]=="conj")):
                        self.conj_set[data[i][0][j]]=self.conj_set[data[i][0][j]]+1
                    elif((data[i][1][j]=="PRT") or (data[i][1][j]=="prt")):
                        self.prt_set[data[i][0][j]]=self.prt_set[data[i][0][j]]+1
                    elif((data[i][1][j]=="PRON") or (data[i][1][j]=="pron")):
                        self.pron_set[data[i][0][j]]=self.pron_set[data[i][0][j]]+1
                    elif((data[i][1][j]=="X") or (data[i][1][j]=="x")):
                        self.x_set[data[i][0][j]]=self.x_set[data[i][0][j]]+1
                    elif((data[i][1][j]==".")):
                        self.dot_set[data[i][0][j]]=self.dot_set[data[i][0][j]]+1
                    else:
                        pass

        
        values_det_set=list(self.det_set.values())
        values_adj_set=list(self.adj_set.values())
        values_adp_set=list(self.adp_set.values())
        values_noun_set=list(self.noun_set.values())
        values_num_set=list(self.num_set.values())
        values_verb_set=list(self.verb_set.values())
        values_adv_set=list(self.adv_set.values())
        values_conj_set=list(self.conj_set.values())
        values_prt_set=list(self.prt_set.values())
        values_pron_set=list(self.pron_set.values())
        values_x_set=list(self.x_set.values())
        values_dot_set=list(self.dot_set.values())
        
        sum_val_det=0
        sum_val_adj=0
        sum_val_adp=0
        sum_val_adv=0
        sum_val_noun=0
        sum_val_num=0
        sum_val_verb=0
        sum_val_conj=0
        sum_val_prt=0
        sum_val_pron=0
        sum_val_x=0
        sum_val_dot=0

        for i in values_det_set:
        	sum_val_det+=i
        for i in values_adj_set:
            sum_val_adj+=i
        for i in values_adp_set:
            sum_val_adp+=i
        for i in values_adv_set:
            sum_val_adv+=i
        for i in values_noun_set:
            sum_val_noun+=i
        for i in values_num_set:
            sum_val_num+=i
        for i in values_verb_set:
            sum_val_verb+=i
        for i in values_conj_set:
            sum_val_conj+=i
        for i in values_prt_set:
            sum_val_prt+=i
        for i in values_pron_set:
            sum_val_pron+=i
        for i in values_x_set:
            sum_val_x+=i
        for i in values_dot_set:
            sum_val_dot+=i
        
        for i in range(len(values_det_set)):
        	values_det_set[i]=values_det_set[i]/sum_val_det
        for i in range(len(values_adj_set)):
            values_adj_set[i]=values_adj_set[i]/sum_val_adj
        for i in range(len(values_adp_set)):
            values_adp_set[i]=values_adp_set[i]/sum_val_adp
        for i in range(len(values_adv_set)):
            values_adv_set[i]=values_adv_set[i]/sum_val_adv
        for i in range(len(values_noun_set)):
            values_noun_set[i]=values_noun_set[i]/sum_val_noun
        for i in range(len(values_num_set)):
            values_num_set[i]=values_num_set[i]/sum_val_num
        for i in range(len(values_verb_set)):
            values_verb_set[i]=values_verb_set[i]/sum_val_verb
        for i in range(len(values_conj_set)):
            values_conj_set[i]=values_conj_set[i]/sum_val_conj
        for i in range(len(values_prt_set)):
            values_prt_set[i]=values_prt_set[i]/sum_val_prt
        for i in range(len(values_pron_set)):
            values_pron_set[i]=values_pron_set[i]/sum_val_pron
        for i in range(len(values_x_set)):
            values_x_set[i]=values_x_set[i]/sum_val_x
        for i in range(len(values_dot_set)):
            values_dot_set[i]=values_dot_set[i]/sum_val_dot
        
        m=0
        for i in set_det:
        	self.det_set[i]=values_det_set[m]
        	m+=1
        m=0
        for i in set_adj:
            self.adj_set[i]=values_adj_set[m]
            m+=1
        m=0
        for i in set_adp:
            self.adp_set[i]=values_adp_set[m]
            m+=1
        m=0
        for i in set_adv:
            self.adv_set[i]=values_adv_set[m]
            m+=1
        m=0
        for i in set_noun:
            self.noun_set[i]=values_noun_set[m]
            m+=1
        m=0
        for i in set_num:
            self.num_set[i]=values_num_set[m]
            m+=1
        m=0
        for i in set_verb:
            self.verb_set[i]=values_verb_set[m]
            m+=1
        m=0
        for i in set_conj:
            self.conj_set[i]=values_conj_set[m]
            m+=1
        m=0
        for i in set_prt:
            self.prt_set[i]=values_prt_set[m]
            m+=1
        m=0
        for i in set_pron:
            self.pron_set[i]=values_pron_set[m]
            m+=1
        m=0
        for i in set_x:
            self.x_set[i]=values_x_set[m]
            m+=1
        m=0
        for i in set_dot:
            self.dot_set[i]=values_dot_set[m]
            m+=1
        
        #self.emis=[self.det_set,self.adj_set,self.adp_set,self.adv_set,self.noun_set,self.num_set,self.verb_set,self.conj_set,self.prt_set,self.pron_set,self.x_set,self.dot_set]
        


    

    # Functions for each algorithm. Right now this just returns nouns -- fix this!
    #

    def ret_dict(self,pos,word):
        if(pos=='det'):
            if(word in self.det_set):
                return self.det_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='adj'):
            if(word in self.adj_set):
                return self.adj_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='adv'):
            if(word in self.adv_set):
                return self.adv_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='adp'):
            if(word in self.adp_set):
                return self.adp_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='noun'):
            if(word in self.noun_set):
                return self.noun_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='num'):
            if(word in self.num_set):
                return self.num_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='verb'):
            if(word in self.verb_set):
                return self.verb_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='conj'):
            if(word in self.conj_set):
                return self.conj_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='prt'):
            if(word in self.prt_set):
                return self.prt_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='pron'):
            if(word in self.pron_set):
                return self.pron_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='x'):
            if(word in self.x_set):
                return self.x_set[word]
            else:
                return 0.000000000000000001
        elif(pos=='.'):
            if(word in self.dot_set):
                return self.dot_set[word]
            else:
                return 0.000000000000000001
        else:
            return 0

    def simplified(self, sentence):
        lst=[]
        for i in sentence:
            lst.append(max_pro([self.det_set,self.adj_set,self.adp_set,self.adv_set,self.noun_set,self.num_set,self.verb_set,self.conj_set,self.prt_set,self.pron_set,self.x_set,self.dot_set],i))
        return lst

    def hmm_viterbi(self, sentence):
        lst=[]
        lst.append(Word(sentence[0],[self.det_set,self.adj_set,self.adp_set,self.adv_set,self.noun_set,self.num_set,self.verb_set,self.conj_set,self.prt_set,self.pron_set,self.x_set,self.dot_set],self.prob_trans,self.initial_prob,0,None))
        for i in range(1,len(sentence)):
            lst.append(Word(sentence[i],[self.det_set,self.adj_set,self.adp_set,self.adv_set,self.noun_set,self.num_set,self.verb_set,self.conj_set,self.prt_set,self.pron_set,self.x_set,self.dot_set],self.prob_trans,self.initial_prob,i,lst[i-1]))
        result_list=[]
        for i in lst:
            i.compute_scores()
        resul=lst[len(lst)-1].ret_maxi_string()
        return resul

    def complex_mcmc(self, sentence):
        initial_pos=rand_pos(sentence)
        pos_list=["det","adj","adp","adv","noun","num","verb","conj","prt","pron","x","."]
        occurences={}
        for i in range(500):
            for j in range(len(sentence)):
                lst1=[]
                if(len(sentence)==1):
                    for pos in pos_list:
                        p=(self.ret_dict(pos,sentence[j])*self.initial_prob[pos.upper()])
                        lst1.append(p)
                elif(j==0):
                    for pos in pos_list:
                        edge1=pos+"-"+initial_pos[1]
                        edge=edge1.upper()
                        p=((self.ret_dict(pos,sentence[0]))*(self.initial_prob[pos.upper()])*(self.prob_trans[edge]))
                        lst1.append(p)
                elif(j==(len(sentence)-1)):
                    for pos in pos_list:
                        edge1=pos+"-"+initial_pos[j-1]
                        edge=edge1.upper()
                        edge2=initial_pos[j-1]+"-"+initial_pos[0]
                        edge2u=edge2.upper()
                        p=((self.ret_dict(pos,sentence[j]))*(self.prob_trans[edge2u])*(self.ret_dict(initial_pos[j-1],sentence[j]))*(self.prob_trans[edge]))
                        lst1.append(p)
                else:
                    for pos in pos_list:
                        edge1=initial_pos[j-1]+"-"+pos
                        edge2=pos+"-"+initial_pos[j+1]
                        edge=edge1.upper()
                        edge2u=edge2.upper()
                        p=((self.ret_dict(pos,sentence[j]))*(self.ret_dict(initial_pos[j-1],sentence[j-1]))*(self.ret_dict(initial_pos[j-1],sentence[j]))*(self.ret_dict(initial_pos[j],sentence[j+1]))*(self.ret_dict(initial_pos[j+1],sentence[j+1]))*(self.prob_trans[edge])*(self.prob_trans[edge2u]))
                        lst1.append(p)

                total=sum(lst1)
                p_dist=cpy_lst(lst1)
                for t in range(len(lst1)):
                    if(total>0):
                        p_dist[t]=p_dist[t]/total
                    else:
                        pass

                cut_off=random.uniform(0,1)
                p_sum=0
                for k in range(len(p_dist)):
                    p_sum+=p_dist[k]
                    if(p_sum>cut_off):
                        initial_pos[j]=pos_list[k]
                        break
                for u in range(len(initial_pos)):
                    if((u,initial_pos[u]) not in occurences):
                        occurences[u,initial_pos[u]]=1
                    else:
                        occurences[u,initial_pos[u]]+=1

        result=[]
        for i in range(len(initial_pos)):
            maxi=0
            pos=""
            for j in pos_list:
                if((i,j) in occurences):
                    if(occurences[i,j]>=maxi):
                        maxi=occurences[i,j]
                        pos=j
            result.append(pos)

        

        return result





    # This solve() method is called by label.py, so you should keep the interface the
    #  same, but you can change the code itself. 
    # It should return a list of part-of-speech labelings of the sentence, one
    #  part of speech per word.
    #
    def solve(self, model, sentence):
        if model == "Simple":
            return self.simplified(sentence)
        elif model == "HMM":
            return self.hmm_viterbi(sentence)
        elif model == "Complex":
            return self.complex_mcmc(sentence)
        else:
            print("Unknown algo!")

