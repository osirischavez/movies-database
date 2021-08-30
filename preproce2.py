import pandas as pd

credits=pd.read_csv("credits.csv")
credits=pd.DataFrame(credits)

n=len(credits)
credits_cast=pd.DataFrame()

data_idcredito=[]
dataid=[]
datamovie=[]
for i in range(0,n):
    cast=credits.iloc[i]['cast']
    cast=eval(cast)   
    for j in range(0,len(cast)):
        dato=(cast[j])
        idcredit=dato['credit_id']
#        idcredit="'"+idcredit+"'"
        id=dato['id']
        data_idcredito.append(idcredit)
        dataid.append(id)
        datamovie.append(credits.iloc[i]['id'])

credits_cast.insert(0,'id_credit',data_idcredito,True)
credits_cast.insert(1,'id_people',dataid,True)
credits_cast.insert(2,'id_movie',datamovie,True)
credits_cast.drop_duplicates(subset='id_credit', keep="first", inplace=True)
credits_cast.to_csv("credits_cast.csv", index= False)

datacreditid=[]
dataid=[]
datajobs=[]
datamovie=[]
eliminar=",'"
credits_crew=pd.DataFrame()
for i in range(0,n):
    crew=credits.iloc[i]['crew']
    crew=eval(crew)   
    for j in range(0,len(crew)):
        dato=(crew[j])
        creditid=dato['credit_id']
#        creditid="'"+creditid+"'"
        id=dato['id']    
        job=dato['job']
        for x in range(len(eliminar)):
            job=job.replace(eliminar[x],"")
#        job="'"+job+"'"
        datacreditid.append(creditid)
        dataid.append(id)
        datajobs.append(job)
        datamovie.append(credits.iloc[i]['id'])    

credits_crew.insert(0,'id_credit',datacreditid,True)
credits_crew.insert(1,'id_people',dataid,True)
credits_crew.insert(2,'job_crew',datajobs,True)
credits_crew.insert(3,'id_movie',datamovie,True)
credits_crew.drop_duplicates(subset='id_credit', keep="first", inplace=True)
credits_crew.to_csv("credits_crew.csv", index= False)

people=pd.DataFrame()
dataid=[]
dataname=[]
eliminar=",'"
eliminar2='"'
for i in range(0,n):
    cast=credits.iloc[i]['cast']
    crew=credits.iloc[i]['crew']
    cast=eval(cast)
    crew=eval(crew)   
    for j in range(0,len(cast)):
        dato=(cast[j])
        name=dato['name']
        for x in range(len(eliminar)):
            name=name.replace(eliminar[x],"")
        for x in range(len(eliminar2)):
            name=name.replace(eliminar2[x],"")
#        name="'"+name+"'"
        id=dato['id']
        dataname.append(name)
        dataid.append(id)
    for j in range(0,len(crew)):
        dato=(crew[j])
        name=dato['name']
        for x in range(len(eliminar)):
            name=name.replace(eliminar[x],"")
#        name="'"+name+"'"
        id=dato['id']
        dataname.append(name)
        dataid.append(id)

people.insert(0,'id',dataid,True)
people.insert(1,'name',dataname,True)
people.drop_duplicates(subset=['id'], keep="first", inplace=True)
people.to_csv("people.csv", index= False)

movies_metadata=pd.read_csv("movies_metadata.csv", low_memory=False)
movies_metadata=pd.DataFrame(movies_metadata)
n=len(movies_metadata)

movies_genres=pd.DataFrame()
dataidgenres=[]
dataname=[]
for i in range(0,n):
    genres=movies_metadata.iloc[i]['genres']
    genres=eval(genres)   
    for j in range(0,len(genres)):
        dato=(genres[j])
        id=dato['id']
        name=dato['name']
#        name="'"+name+"'"
        dataidgenres.append(id)
        dataname.append(name)

movies_genres.insert(0,'id',dataidgenres,True)
movies_genres.insert(1,'name_gentes',dataname,True)
movies_genres.drop_duplicates(subset=None, keep="first", inplace=True)
movies_genres.to_csv("movies_genres.csv", index= False)

dataid=[]
dataidgenres=[]
for i in range(0,n):
    genres=movies_metadata.iloc[i]['genres']
    genres=eval(genres)
    for j in range(0,len(genres)):
        dato=(genres[j])
        idgenres=dato['id']
        dataidgenres.append(idgenres)
        dataid.append(movies_metadata.iloc[i]['id'])
        

rel_movies_genres=pd.DataFrame()
rel_movies_genres.insert(0,'id_genres',dataidgenres,True)
rel_movies_genres.insert(1,'id_movie',dataid,True)
rel_movies_genres.drop_duplicates(subset= None, keep="first", inplace=True)
rel_movies_genres.to_csv("rel_movies_genres.csv", index= False )

movies=pd.DataFrame()
dataidmovie=[]
datatitle=[]
datavote=[]
datacount=[]
eliminar1="',"
eliminar2='"'
for i in range(0,n):
    idmovie=movies_metadata.iloc[i]['id']
    title=movies_metadata.iloc[i]['title']
    vote=movies_metadata.iloc[i]['vote_average']
    votecount=movies_metadata.iloc[i]['vote_count']
    dataidmovie.append(idmovie)
    title=str(title)
    for x in range(len(eliminar1)):
        title=title.replace(eliminar1[x],"")
    for x in range(len(eliminar2)):
        title=title.replace(eliminar2[x],"")
#    title="'"+title+"'"
    datatitle.append(title)
    datavote.append(vote)
    datacount.append(votecount)

movies=pd.DataFrame()
movies.insert(0,'id',dataidmovie,True)
movies.insert(1,'title',datatitle,True)
movies.insert(2,'vote_avarage',datavote,True)
movies.insert(3,'vote_count',datacount,True)
movies.drop_duplicates(subset=['id'], keep="first", inplace=True)

movies.to_csv("movies.csv", index= False)