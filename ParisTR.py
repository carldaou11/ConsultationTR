# Importation des bibliothèques
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st
from tabulate import tabulate

# Chargement des données
elections = pd.read_csv("Votation-2023-04-02.csv")

# Remplacer les espaces par des underscores dans les noms de colonnes
elections.columns = [col.replace(' ', '_') for col in elections.columns]

# Mettre en forme les noms de colonnes
elections.columns = elections.columns.str.title()

# Conversion des colonnes en numérique
numeric_columns = ['Inscrits', 'Emargements', 'Votants', 'Exprimes', 'Contre', 'Pour']
for col in numeric_columns:
    if elections[col].dtype == 'O':
        elections[col] = pd.to_numeric(elections[col].str.replace(',', ''), errors='coerce')
st.title("Résultats des Élections 2023 - Pour ou contre les trottinettes en libre-service à Paris? #")
image_url = "https://img.lemde.fr/2023/04/02/0/0/5472/3648/1440/960/60/0/48adfba_5910791-01-06.jpg"  # Remplacez cela par l'URL réelle de 

# Affichage de l'image
st.image(image_url, caption='Les trottinettes en libre-service, comme celles de la marque Lime, propriété de Uber, disparaitrons à la fin des contrats qui lient les loueurs à la capitale. © AFP', use_column_width=True)

st.markdown(
    """
    Rapport réalisé par Carl DAOU
   
    
    Le dimanche 2 avril 2023, la ville de Paris a organisé  une consultation citoyenne cruciale 
    sur le futur de l'utilisation des trottinettes en libre-service.
    
    Cette votation consultative, sous le vigilant contrôle d'une commission indépendante, a permis 
    aux citoyens de s'exprimer sur cette question clé pour le tissu urbain parisien. Quelle est l'ampleur de l'engagement citoyen dans la consultation sur l'avenir des trottinettes en libre-service à Paris, et quels facteurs influent sur les niveaux de participation et les résultats?
    
    Le jeu de données "votation-trottinette-2023" dévoile les résultats complets de cette démarche démocratique, 
    allant du nombre d'inscrits aux votes exprimés, en passant par les opinions "Pour" et "Contre".
    
    - **Identifiant du jeu de données:** votation-trottinette-2023 accessible sur https://opendata.paris.fr/explore/dataset/votation-trottinette-2023/information/
    - **Thèmes:** Citoyenneté
    - **Mots clés:** résultats, vote, trottinettes
    - **Licence:** Open Database License (ODbL)
    - **Langue:** Français
    - **Producteur:** Direction de la Démocratie, des Citoyen.ne.s et des Territoires - Ville de Paris
    - **Territoire:** Paris
    
    Un lien pour tout savoir sur le fonctionnement du bureau de vote en France: https://www.vie-publique.fr/questions-reponses/269425-le-fonctionnement-du-bureau-de-vote-foire-aux-questions-faq
    
    Explorez les données ci-dessous pour découvrir les nuances des opinions exprimées par les citoyens parisiens.
    
    **Notre jeu de données contient les colonnes suivantes  :**
    
    - **Inscrits :**
      - Nombre total de personnes éligibles et inscrites sur les listes électorales pour participer à l'élection ou au vote.
      
    - **Votants :**
      - Nombre de personnes qui ont effectivement participé au vote.
      
    - **Blancs :**
      - Nombre de bulletins blancs, c'est-à-dire de votes exprimés de manière neutre sans choisir de candidat ou d'option.
      
    - **Nuls :**
      - Nombre de votes nuls, généralement dus à des erreurs de marquage ou à des bulletins non conformes aux règles électorales.
      
    - **Exprimés :**
      - Nombre de votes valides, c'est-à-dire le total des votes exprimés qui ont été pris en compte dans le résultat final.
      
    - **Contre :**
      - Nombre de votes exprimés contre une proposition ou un candidat spécifique.
      
    - **Pour :**
      - Nombre de votes exprimés en faveur d'une proposition ou d'un candidat spécifique.
      
    - **Participation (a été  ajouter) :**
      - Pourcentage des inscrits qui ont effectivement participé au vote. Calculé comme (Votants / Inscrits) * 100.
    """
    
)




# Affichage des résultats clés et de l'image
# Calcul des chiffres clés
total_participation = round((elections['Votants'].sum() / elections['Inscrits'].sum()) * 100, 2)
ratio_blancs_nuls = round((elections['Blancs'].sum() + elections['Nuls'].sum()) / elections['Exprimes'].sum() * 100, 2)
ratio_pour = round(elections['Pour'].sum() / elections['Exprimes'].sum() * 100, 2)
ratio_contre = round(elections['Contre'].sum() / elections['Exprimes'].sum() * 100, 2)

# Secteur administratif avec le plus haut et le plus bas taux de participation
# Calcul du taux de participation
elections['Participation'] = round((elections['Votants'] / elections['Inscrits']) * 100, 2)
max_participation_sector = elections.loc[elections['Participation'].idxmax()]['Secteurs_Administratifs']
min_participation_sector = elections.loc[elections['Participation'].idxmin()]['Secteurs_Administratifs']

# Nombre total d'inscrits et de votants
total_inscrits = elections['Inscrits'].sum()
total_votants = elections['Votants'].sum()

# Affichage des chiffres clés
st.info(f"Taux de Participation Global : {total_participation}%")
st.info(f"Ratio de Votes Blancs et Nuls : {ratio_blancs_nuls}%")
st.info(f"Ratio de Votes 'Pour' : {ratio_pour}%")
st.info(f"Ratio de Votes 'Contre' : {ratio_contre}%")
st.info(f"Secteur avec le Plus Haut Taux de Participation : {max_participation_sector}")
st.info(f"Secteur avec le Plus Bas Taux de Participation : {min_participation_sector}")
st.info(f"Nombre Total d'Inscrits : {total_inscrits}")
st.info(f"Nombre Total de Votants : {total_votants}")

        
        
# Définir la largeur maximale des colonnes pour éviter la troncature
st.set_option('deprecation.showPyplotGlobalUse', False)
pd.set_option('display.max_colwidth', None)


# Sélection des colonnes spécifiques pour le tableau récapitulatif
table_data = elections[['Secteurs_Administratifs', 'Inscrits', 'Votants', 'Blancs', 'Nuls', 'Exprimes', 'Contre', 'Pour', 'Participation']]

# Formater la colonne 'Participation' pour inclure le symbole '%'
table_data['Participation'] = table_data['Participation'].apply(lambda x: f"{x:.2f}%")

# Calcul du pourcentage de votes "Pour" et "Contre" par zone
table_data['Pourcentage_Pour'] = round((table_data['Pour'] / table_data['Exprimes']) * 100, 2)
table_data['Pourcentage_Contre'] = round((table_data['Contre'] / table_data['Exprimes']) * 100, 2)

# Formater les colonnes de pourcentage pour inclure le symbole '%'
table_data['Pour'] = table_data.apply(lambda row: f"{row['Pour']} ({row['Pourcentage_Pour']}%)", axis=1)
table_data['Contre'] = table_data.apply(lambda row: f"{row['Contre']} ({row['Pourcentage_Contre']}%)", axis=1)

# Supprimer les colonnes de pourcentage inutiles
table_data = table_data.drop(['Pourcentage_Pour', 'Pourcentage_Contre'], axis=1)

# Affichage du tableau récapitulatif avec Streamlit sans l'index
st.write('Les données utilisées pour le projet:')
st.table(table_data.set_index('Secteurs_Administratifs'))



#FIGURE 1 Création du graphique avec Plotly Express
fig1 = px.bar(elections.sort_values(by='Inscrits', ascending=True), 
              x='Secteurs_Administratifs', 
              y=['Inscrits', 'Votants'], 
              title='Comparaison entre les personnes inscrites et le nombre de votes par secteur administratif:', 
              barmode='group',
              color_discrete_sequence=['blue', 'orange'])  # Palette de couleurs

# Renommer l'axe des y
fig1.update_layout(yaxis_title='Nombre de personnes')

# Affichage du graphique dans Streamlit
st.plotly_chart(fig1)

# Analyse de base
st.write("""
Analyse :
- La barre bleue représente le nombre d'inscrits dans chaque secteur administratif.
- La barre orange représente le nombre total de votes dans chaque secteur administratif.
- Les facteurs possibles justifiants l'écart entre inscrits (1,382,322) et votants (103,084) :
       **Le manque d'information sur le processus de consultation**
        **et le besoin d'efforts supplémentaires pour mobiliser les électeurs**
""")





#FIGURE 2
# Calculer la colonne 'Non_Votants' comme la différence entre 'Inscrits' et 'Votants'
elections['Non_Votants'] = elections['Inscrits'] - elections['Votants']

#FIGURE 1 Création du graphique avec Plotly Express
fig1 = px.bar(elections.sort_values(by='Inscrits', ascending=True), 
              x='Secteurs_Administratifs', 
              y=['Inscrits', 'Votants', 'Non_Votants'],  # Ajout de la colonne 'Non_Votants'
              title='Comparaison entre les personnes inscrites, les votants et les non-votants par secteur administratif:', 
              barmode='stack',
              color_discrete_sequence=['blue', 'orange', 'gray'])  # Palette de couleurs

# Renommer l'axe des y
fig1.update_layout(yaxis_title='Nombre de personnes')

# Affichage du graphique dans Streamlit
st.plotly_chart(fig1)

# Analyse de base
st.write("""
Analyse :
- La barre bleue représente le nombre d'inscrits dans chaque secteur administratif.
- La barre orange représente le nombre total de votes dans chaque secteur administratif.
- La barre grise représente le nombre de non-votants (différence entre inscrits et votants) qui ont été nombreux lors de cette consultation.
""")


# Comparaison du nombre de votants par secteur administratif en treemap avec informations affichées par défaut et couleur personnalisée
fig2_treemap = px.treemap(elections.sort_values(by='Votants', ascending=True), 
                          path=['Secteurs_Administratifs'], 
                          values='Votants',
                          title='Comparaison du nombre de votants par secteur administratif:',
                          color='Votants',  # Utiliser la colonne 'Votants' pour définir la couleur
                          color_continuous_scale='blues',  # Palette de couleurs
                          hover_data=['Votants'])  # Retirer cette ligne si vous ne voulez pas d'information au survol

# Affichage du treemap dans Streamlit
st.plotly_chart(fig2_treemap)
st.write("""
Chaque bloc rectangulaire représente un secteur administratif, sa taille étant proportionnelle au nombre de votants. La couleur de chaque bloc est attribuée en fonction du nombre de votants, allant des tons plus clairs aux tons plus foncés. Ainsi, les secteurs avec une participation élevée se démarquent par des couleurs plus soutenues. En survolant chaque bloc, vous pouvez obtenir des informations détaillées, notamment le nombre exact de votants dans chaque secteur. Cette représentation permet une compréhension rapide des disparités de participation entre les différents quartiers parisiens.
""")

# Comparaison des votes Pour et Contre par secteur administratif
#st.write("Comparaison des votes Pour et Contre par secteur administratif")
fig3 = px.bar(elections.sort_values(by='Contre', ascending=True), x='Secteurs_Administratifs', y=['Pour', 'Contre'],title='Comparaison des votes Pour et Contre par secteur administratif:', barmode='group')
st.plotly_chart(fig3)

# Répartition des votes (Pour/Contre) par type de scrutin
#st.write("Répartition des votes (Pour/Contre) par type de scrutin")
scrutin_votes = elections.groupby('Scrutin').agg({'Pour': 'sum', 'Contre': 'sum'}).reset_index()
melted_votes = pd.melt(scrutin_votes, id_vars=['Scrutin'], value_vars=['Pour', 'Contre'], var_name='Catégorie', value_name='Nombre de votes')
fig4 = px.pie(melted_votes, names='Catégorie', values='Nombre de votes', title='Répartition des votes (Pour/Contre) par type de scrutin:', labels={'Nombre de votes': 'Nombre de votes'}, color='Catégorie', color_discrete_map={'Pour': 'blue', 'Contre': 'red'}, hole=0.5)
st.plotly_chart(fig4)

# Répartition des votes (Pour/Contre/Blancs/Nuls) par type de scrutin
#st.write("Répartition des votes (Pour/Contre/Blancs/Nuls) par type de scrutin")
scrutin_votes = elections.groupby('Scrutin').agg({'Pour': 'sum', 'Contre': 'sum', 'Blancs': 'sum', 'Nuls': 'sum'}).reset_index()
melted_votes = pd.melt(scrutin_votes, id_vars=['Scrutin'], value_vars=['Pour', 'Contre', 'Blancs', 'Nuls'], var_name='Catégorie', value_name='Nombre de votes')

st.write("""
En somme, 103 084 citoyens parisiens ont participé à cette consultation historique, représentant ainsi 7,46% des inscrits sur les listes électorales de la ville. Suite à cette expression démocratique, la ville de Paris s'apprête à devenir la première capitale européenne à mettre fin à l'usage des trottinettes en libre-service.
""")


# Votes blancs et nuls par secteur administratif
#st.write("Votes blancs et nuls par secteur administratif")
sorted_df1 = elections.sort_values(by='Nuls', ascending=True)
fig6 = px.bar(sorted_df1, x='Secteurs_Administratifs', y=['Blancs', 'Nuls'], title='Votes blancs et nuls par secteur administratif:', labels={'value': 'Nombre de votes', 'variable': 'Catégorie'}, color_discrete_map={'Blancs': 'blue', 'Nuls': 'orange'}, barmode='stack')
st.plotly_chart(fig6)

# Taux de participation par secteur administratif
#st.write("Taux de participation par secteur administratif")
sorted_df = elections.sort_values(by='Participation', ascending=True)
fig7 = px.bar(sorted_df, x='Participation', y='Secteurs_Administratifs', orientation='h', title='Taux de participation par secteur administratif:', labels={'Participation': 'Taux de participation (%)', 'Secteurs_Administratifs': 'Secteur administratif'}, color='Participation', text='Participation', color_continuous_scale='reds')
fig7.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
fig7.update_layout(yaxis=dict(showgrid=False, showline=False, showticklabels=True))
st.plotly_chart(fig7)

# Ajouter une nouvelle colonne représentant la somme des exprimés et des inscrits
elections['Exprimes_plus_Inscrits'] = elections['Exprimes'] + elections['Inscrits']
st.write("""
Avec un taux de participation global de seulement 7.46%, cette consultation met en évidence un défi majeur dans la réalisation d'une démocratie participative pleinement représentative. Les variations significatives des taux de participation entre les secteurs, allant de 11.35% dans le 6e arrondissement à 5.86% dans le 19e, mettent en lumière l'importance de considérer les dynamiques locales pour des campagnes de mobilisation plus efficaces. 
Le fait que la consultation ait eu lieu un dimanche pourrait avoir influencé les résultats. Une consultation organisée un dimanche peut parfois rencontrer une participation plus faible en raison des engagements personnels des votants tels que des obligations familiales, des activités de loisirs, ou tout simplement la préférence de consacrer ce jour à des loisirs et au repos. L'écart entre le nombre d'inscrits et de votants indique une opportunité d'amélioration des campagnes d'information et de mobilisation, suggérant la nécessité de stratégies innovantes pour encourager la participation de tous les citoyens éligibles. En réponse, des recommandations incluent le développement de campagnes d'information ciblées, l'implication active des communautés locales dans le processus décisionnel, et une étude approfondie des facteurs de rejet des trottinettes en libre-service pour guider les politiques futures. 

""")
