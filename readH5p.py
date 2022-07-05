#!/usr/bin/env python


urls = [
        {"label": "Transversal",
         "url": "https://raw.githubusercontent.com/call-learning/H5P.SoftSkills.H5P/master/bachelor-transversal/content/content.json"},
        {"label": "Informational",
         "url": "https://raw.githubusercontent.com/call-learning/H5P.SoftSkills.H5P/master/bachelor-informational/content/content.json"}
        ]

import json, requests, os

# get content.json 
for path in ["contents", "outs"]:
    isExist = os.path.exists(path)
    if not isExist:
      os.makedirs(path)
for url in urls:
    r = requests.get(url['url'], allow_redirects=True)
    open('contents/%s' % url['label'], 'wb').write(r.content)
    data = r.json()

    out = open("outs/%s.html" % url['label'], "w")


    nbPart = 1
    for i in data['questionsByCompetencyAndSubCompetencies']:
        print("%s. %s"% (nbPart,i['label']))
        out.write("%s. %s\n"% (nbPart,i['label']))
        nbSubPart = 1
        for j in i['subCompetencies']:
            print("%s.%s %s"% (nbPart,nbSubPart,j['label']))
            out.write("%s.%s %s\n"% (nbPart,nbSubPart,j['label']))
            res = []
            for k in j['contexts']:
                for q in k['questions']:
                    if 'resources' in q:
                        res += q['resources']
            for r in res:
                print(r['content'])
                out.write("%s\n" %r['content'])
            nbSubPart += 1

        nbPart += 1

    out.close()
