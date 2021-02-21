from recycable import *
from InfoRetriever import *
from Image import *

Im1 = Image()
#labels_im1 = []
#Im1.capture()
Im1.capture_bis()
Im1.findLabels()

R = Recyable()
I = InfoRetriever(R.getRecycables())
l=[]
for i in Im1.labels[:8] :
    #print(I.findMatching(i.description))
    l.append(I.findMatching(i.description))
Sort_Tuple(l)
print(l)



