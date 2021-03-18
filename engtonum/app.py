#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def abc():
    return render_template('engtonum.html')

@app.route('/detail',methods=['GET','POST'])
def xyz():
    if request.method=='POST':
        x=request.form['a']
        y=x.lower()
        l=y.split()
        a={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'forteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,'thirty':30, 'fourty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100}

        if len(l)==1:                                 # five, twenty, hundred
            s= a[l[0]]

        elif len(l)==2:
            if a[l[0]] in range(0,10):              # five hundred 
                s= a[l[0]]*100
            else:
                s= a[l[0]]+a[l[1]]              # seventy nine

        elif len(l)==3:
            s= a[l[0]]*100+a[l[2]]          # five hundred fifteen


        elif len(l)==4:
            s= a[l[0]]*100+a[l[2]]+a[l[3]]
        
    return render_template('engtonum.html',answer=s)

if __name__=='__main__':
    app.run()


# In[ ]:




