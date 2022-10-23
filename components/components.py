import streamlit.components.v1 as components
import os
#col_names = ['name', 'number', 'time', 'room', 'instructor']
# {'ARHU 101 - The Art of Interpretation: Written Texts': {'001-SEM': {'section': 'Seven Wk 1', 'number': '1076', 'time': ['MoWe 14:45 - 17:15', 'TuTh 20:10 - 21:10'], 'room': ['TBA', 'TBA'], 'instructor': ['Caio Yurgel', 'Caio Yurgel'], 'date': ['2023/01/09 - 2023/03/02', '2023/01/09 - 2023/03/02']}}}
# {'BEHAVSCI 101 - Introduction to Behavioral Science': {'001-SEM': {'section': 'Seven Wk 1', 'number': '1034', 'time': ['MoTuWeTh 08:30 - 09:45', 'TuTh 19:00 - 20:00'], 'room': ['TBA', 'TBA'], 'instructor': ['Claudia Nisa', 'Claudia Nisa'], 'date': ['2023/01/09 - 2023/03/02', '2023/01/09 - 2023/03/02']}}, 'BEHAVSCI 102 - Mechanisms of Human Behavior': {'001-SEM': {'section': 'Seven Wk 2', 'number': '1137', 'time': ['MoWe 08:30 - 11:00', 'TuTh 19:00 - 20:00'], 'room': ['TBA', 'TBA'], 'instructor': ['Gergely Horvath', 'Gergely Horvath'], 'date': ['2023/03/20 - 2023/05/11', '2023/03/20 - 2023/05/11']}}, 'BEHAVSCI 201 - Individuals and Their Decisions': {'001-SEM': {'section': 'Seven Wk 2', 'number': '1143', 'time': ['MoTuWeTh 10:00 - 11:15', 'MoWe 19:00 - 20:00'], 'room': ['TBA', 'TBA'], 'instructor': ['Claudia Nisa, Yanran Yang', 'Claudia Nisa, Yanran Yang'], 'date': ['2023/03/20 - 2023/05/11', '2023/03/20 - 2023/05/11']}}, 'BEHAVSCI 202 - Institutions, Groups, and Society': {'001-SEM': {'section': 'Seven Wk 1', 'number': '1035', 'time': ['MoTuWeTh 08:30 - 09:45', 'TuTh 19:00 - 20:00'], 'room': ['TBA', 'TBA'], 'instructor': ['Kristinn Mar', 'Kristinn Mar'], 'date': ['2023/01/09 - 2023/03/02', '2023/01/09 - 2023/03/02']}}, 'BEHAVSCI 203 - Comparative Analysis of Behavior': {'001-SEM': {'section': 'Seven Wk 2', 'number': '1184', 'time': ['MoWe 14:45 - 17:15', 'TuTh 20:10 - 21:10'], 'room': ['TBA', 'TBA'], 'instructor': ['Wen Zhou', 'Wen Zhou'], 'date': ['2023/03/20 - 2023/05/11', '2023/03/20 - 2023/05/11']}}, 'BEHAVSCI 301 - Computational Neuroscience': {'001-SEM': {'section': 'Seven Wk 2', 'number': '1162', 'time': ['MoWe 07:15 - 08:15', 'TuTh 12:00 - 14:30'], 'room': ['TBA', 'TBA'], 'instructor': ['Christoph Weidemann', 'Christoph Weidemann'], 'date': ['2023/03/20 - 2023/05/11', '2023/03/20 - 2023/05/11']}}, 'BEHAVSCI 401 - Moving Beyond Nudges': {'001-SEM': {'section': 'Seven Wk 2', 'number': '1138', 'time': ['MoWe 19:00 - 20:00', 'TuTh 08:30 - 11:00'], 'room': ['TBA', 'TBA'], 'instructor': ['Irina Soboleva', 'Irina Soboleva'], 'date': ['2023/03/20 - 2023/05/11', '2023/03/20 - 2023/05/11']}}, 'BEHAVSCI 402 - Judgement and Decision Making': {'001-SEM': {'section': 'Seven Wk 1', 'number': '1092', 'time': ['MoWe 21:20 - 22:20', 'TuTh 12:00 - 14:30'], 'room': ['TBA', 'TBA'], 'instructor': ['Wen Zhou', 'Wen Zhou'], 'date': ['2023/01/09 - 2023/03/02', '2023/01/09 - 2023/03/02']}}}
## Importing 
def CourseShown(data):
    html=getimport()
    for coursename, value in data.items():
        
        html +=renderHtml('table',{'ClassName':coursename})
    print(html)
    components.html(
        """
        %s
        """ %html, height=1200,width=700,scrolling=True
    )


def renderHtml(template_html, dict):
    template_html_path = os.path.dirname(os.path.abspath(__file__))+'/HTML/%s.html' % template_html
    with open (template_html_path,'r') as f:
        html = f.read()
    for key,value in dict.items():
        html=html.replace("{{%s}}"% key,str(value))
    return html

def getimport():
    return """<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
  integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
  integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
  integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>"""


if __name__=="__main__":
    print(os.path.abspath(__file__))
