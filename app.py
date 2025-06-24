import streamlit as st
import random

st.set_page_config(page_title="🔥 Gioco Erotico per Coppie 🔥", layout="centered")

st.title("🔥 Gioco Erotico per Coppie - Sfide Hard 🔥")
st.markdown("""
Giocate a turno: premi il bottone per lui o per lei e ricevi una sfida da fare.
La seduzione, il controllo e il piacere sono la chiave del gioco.
Divertitevi a scoprire nuove sensazioni insieme!  
**NB:** Consenso e rispetto sempre al primo posto.
""")

sfide_per_lei = [
    "Legami piedi e le mani: leccami SOLO DAVANTI PER 5 minuti",
    "Legami piedi e mani: leccami solo dietro per 3 minuti e le mani le usi davanti",
    "Mi devi legare le mani, mettere a pecora e leccarla con un dito dietro. Vai avanti per 5 minuti. In 5 minuti puoi leccarla solo un minuto",
    "Mi fai stendere a pancia in alto (a stella), mi schiacci la pancia, mi bendi gli occhi e inizi a toccarmi piano, tipo massaggio.. dopo un po’ con una mano continui e con l’altra un dito dietro",
    "Mi bendi gli occhi e mi tappi la bocca, mi morsichi il collo, le tette, la pancia",
    "Mi leghi i piedi, li metti alla tua spalla, inizi a leccarli e a morderli",
    "Devi guardare un massaggio sui porno, prendere su punto e provare a farlo su di me",
    "Devo riempirti di olio, massaggiare e poi guardare mentre mi tocco da sola per 5 minuti",
    "Devi mettere la panna montata sul culo, se vuoi anche le fragole, e mangiarle direttamente da lì",
    "Con un cubetto di ghiaccio in bocca, parti dalla bocca e arrivi ai piedi",
    # Aggiunte mie:
    "Ti leghi i polsi dietro la schiena e ti muovi solo col bacino per 10 minuti",
    "Ti massaggio i piedi con olio caldo mentre mi guardi senza poter toccarmi",
    "Mi fai baciare ogni dito dei tuoi piedi lentamente uno per uno",
    "Mi metti a pecora e mi fai un massaggio lento e profondo sulla schiena e le chiappe",
    "Usi il tuo corpo come una frusta, sfregandoti su di me con controllo e passione",
    "Ti lego le mani sopra la testa e ti coccolo i piedi per 7 minuti senza fermarti",
    "Indossi le calze più sensuali che hai e mi comandi di baciartele e leccartele per 5 minuti",
    "Mi tocchi e mi guardi mentre ti rilasso le gambe, poi passi al bacino con lentezza",
    "Ti impongo di non fare rumore mentre ti tocco ogni centimetro del corpo",
    "Ti lecco piano la schiena, scendendo verso il sedere e ti costringo a trattenere il respiro"
]

sfide_per_lui = [
    "Devi legarmi i polsi, farmi una sega mentre mi metti i piedi al collo e in faccia e li muovi, ma non mi fai venire mai.",
    "Devi letteralmente sederti sulla mia faccia e cercare di soffocarmi, io se non respiro più batto la mano sulla tua gamba",
    "Devi essere aggressiva e farmi male, tirandomi i capelli, mettendomi le dita in bocca, e comandando la mia testa dai capelli tirati, per leccartela.",
    "Seduti uno di fronte all'altro, tu ti tocchi, io pure, ma non posso venire, e giochi coi piedi per catturare la mia attenzione, facendomeli baciare ogni tanto.",
    "Tu a pancia in giù, mi fai letteralmente impazzire muovendo il culo e stringendomelo dalle chiappe, e mi fai venire così",
    "Mi bendi, usi varie parti del corpo da avvicinare e sfiorarmi la faccia, mentre mi fai una sega. Se non indovino smetti di farmela e vai avanti.",
    "Devi obbligarmi a farmi mangiare del cibo dal tuo corpo, sulla vagina bagnata soprattutto, devo leccare via tutto.",
    "Mi leghi il collo, e mi tiri dove vuoi: in mezzo alle tue gambe, sui piedi, sul culo",
    "Mi scopi tu, e quando sto per venire, ti fermi per 10 volte. Devi vedermi il cazzo esplodere",
    "Devi letteralmente strusciarmi la vagina in faccia, non 69 ma dal davanti, devi bagnarmi completamente la faccia, e spesso soffocarmi. Io non posso toccarmi",
    # Aggiunte mie:
    "Mi bendi gli occhi e mi fai toccare solo con i piedi, non posso usare le mani",
    "Devo massaggiare il tuo corpo con olio caldo mentre tu mi dici cosa fare",
    "Devo sedermi tra le tue gambe e farmi comandare usando solo il corpo, senza parlare",
    "Mi metti a pecora e inizi a mordermi il collo mentre con le mani giochi con i miei piedi",
    "Mi ordini di non venire mai per 10 minuti mentre mi giochi con le chiappe e il culo",
    "Mi fai sedere con la faccia tra le tue gambe e mi comandi di leccarti senza fermarmi",
    "Mi costringi a toccarmi ma non a venire, mentre tu giochi con i piedi sulla mia faccia",
    "Devo baciare lentamente ogni centimetro delle tue gambe fino a risalire al bacino",
    "Mi fai massaggiare i tuoi piedi, poi mi metti la testa sotto di te per un’ora"
]

def nuova_sfida(chi: str):
    if chi == "lei":
        return random.choice(sfide_per_lei)
    else:
        return random.choice(sfide_per_lui)

# Memorizza le sfide già usate per evitare ripetizioni
if "sfide_lei_giocate" not in st.session_state:
    st.session_state.sfide_lei_giocate = set()
if "sfide_lui_giocate" not in st.session_state:
    st.session_state.sfide_lui_giocate = set()

def pesca_sfida(chi: str):
    lista = sfide_per_lei if chi == "lei" else sfide_per_lui
    giocate = st.session_state.sfide_lei_giocate if chi == "lei" else st.session_state.sfide_lui_giocate

    if len(giocate) == len(lista):
        # Se abbiamo finito tutte le sfide, resettiamo
        giocate.clear()

    disponibili = [i for i in range(len(lista)) if i not in giocate]
    scelta_idx = random.choice(disponibili)
    giocate.add(scelta_idx)
    return lista[scelta_idx]

col1, col2 = st.columns(2)

with col1:
    if st.button("🎲 Sfida per Lei"):
        sfida = pesca_sfida("lei")
        st.markdown(f"### Per Lei: \n{sfida}")

with col2:
    if st.button("🎲 Sfida per Lui"):
        sfida = pesca_sfida("lui")
        st.markdown(f"### Per Lui: \n{sfida}")
