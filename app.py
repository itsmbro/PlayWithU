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

# Piaceri originali PER LEI (come forniti da te)
sfide_per_lei = [
    "Legami piedi e le mani : leccami SOLO DAVANTI PER 5 minuti",
    "⁠legami piedi e mani: leccami solo dietro per 3 minuti e le mani le usi davanti",
    "⁠ mi devi legare le mani, mettere a pecora e leccarla con un dito dietro. Vai avanti per 5 minuti. In 5 minuti puoi leccarla solo un minuto",
    "⁠mi fai straniare a pancia in altro (a stella) mi schiacci la pancia, mi bendi gli occhi e inizi a toccarmi, Piano, tipo un massaggio.. dopo un po’ con una mano continui e con l’altra un dito dietro",
    "⁠mi bendi gli occhi e mi tappi la bocca, mi morsichi il collo, le tette, la pancia",
    "⁠mi leghi i piedi, li metti alla tua spalle, inizi a leccarli e a morderli",
    "⁠devi guardare un massaggio sui porno, prendere su punto e provare a farlo su di me",
    "⁠devo riempiri di olio, massaggiare e poi guardare mentre mi tocco da sola per 5 minuti",
    "⁠devi mettere la panna montata sul culo, se vuoi anche le fragole, e mangiate direttamente da lì",
    "⁠con un cubetto di ghiaccio in bocca, parti dalla bocca e arrivi ai piedi",
    "Voglio che mi guarda per 5 minuti mentre uno il vibratore",
    "Voglio che mente uso il vibratore tu usi le mani fino a quando non vengo, puoi ogni tanto smettere per farti una sega",
    "Voglio che ti fai una sega per  5 minuti mentre mi massaggi i piedi con l’altra mano",
    "Voglio che mi lecchi i piedi e li piedi mentre ti tocchi, e vai avanti fino a quando non stai per venire"
]

# Nuove sfide originali PER LEI, ispirate ai suoi piaceri (10)
sfide_per_lei_2 = [
    "Ti lego le mani sopra la testa e ti massaggio lentamente le cosce fino al bacino per 10 minuti",
    "Con le mani legate, devi ascoltare solo la mia voce mentre ti guido in un gioco sensoriale",
    "Ti massaggio i piedi con olio caldo mentre sei bendata e non puoi muoverti",
    "Mi costringi a leccarti ogni dito dei piedi uno per uno, con calma e attenzione",
    "Mi metti a pecora e con le dita accarezzi la schiena e le chiappe fino a farmi rabbrividire",
    "Usi il tuo corpo come una frusta, sfregandoti su di me con controllo e passione per 7 minuti",
    "Indossi le calze più sensuali che hai e mi ordini di baciartele e leccartele senza mai fermarmi",
    "Mi obblighi a non fare rumore mentre ti tocco ogni centimetro del corpo",
    "Ti lecco lentamente la schiena scendendo verso il sedere e ti costringo a trattenere il respiro",
    "Mi fai un massaggio lento e profondo con olio caldo, mentre mi bendi e non posso vedere nulla"
]

# Piaceri originali PER LUI (come forniti da te)
sfide_per_lui = [
    "devi legarmi i polsi, farmi una sega mentre mi metti i piedi al collo e in faccia e li muovi, ma non mi fai venire mai.",
    "devi letteralmente sederti sulla mia faccia e cercare di soffocarmi, io se non respiro piu batto la mano sulla tua gamba",
    "devi essere aggressiva e farmi male, tirandomi i capelli, mettendomile dita in bocca, e comandando la mia testa dai capelli tirati, per leccartela.",
    "seduti uno di fronte all'altro, tu ti tocchi, io pure, ma non posso venire, e giochi coi piedi per catturare la mia attenzione, facendomeli baciare ogni tanto.",
    "tu a pancia in giu, mi fai letteralmente impazzire muovendo il culo e stringendomelo dalle chiappe, e mi fai venire così",
    "mi bendi, usi varie parti del corpo da avvicinare e sfiorarmi la faccia, mentre mi fai una sega. se non indovino smetti di farmela e vai avanti.",
    "devi obbligarmi a farmi mangiare del cibo dal tuo corpo, sulla vagina bagnata soprattutto, devo leccare via tutto.",
    "mi leghi il collo, e mi tiri dove vuoi: in mezzo alle tue gambe, sui piedi, sul culo",
    "mi scopi tu, e quando sto per venire, ti fermi per 10 volte. devi vedermi il cazzo esplodere",
    "devi letteralmente strusciarmi la vagina in faccia, non 69 ma dal davanti, devi bagnarmi completamente la faccia, e spesso soffocarmi. io non posso toccarmi"
]

# Nuove sfide originali PER LUI, ispirate ai suoi piaceri (10)
sfide_per_lui_2 = [
    "Mi bendi gli occhi e mi fai toccare solo con i piedi, proibendomi di usare le mani per 5 minuti",
    "Devo massaggiare il tuo corpo con olio caldo mentre mi dai ordini precisi su cosa fare",
    "Mi metti a pecora e inizi a mordermi il collo mentre giochi con i miei piedi con le mani",
    "Mi ordini di non venire mai per 10 minuti mentre mi giochi con le chiappe e il culo",
    "Mi fai sedere con la faccia tra le tue gambe e mi comandi di leccarti senza mai fermarmi",
    "Mi costringi a toccarmi ma non a venire, mentre tu giochi con i piedi sulla mia faccia",
    "Devo baciare lentamente ogni centimetro delle tue gambe fino a risalire al bacino",
    "Mi fai massaggiare i tuoi piedi, poi mi metti la testa sotto di te per un’ora",
    "Mi trascini per la stanza legato solo con una sciarpa, mentre io devo obbedire ai tuoi comandi",
    "Devo supplicarti di lasciarmi andare mentre mi tieni fermo con mani e piedi legati"
]

# Funzioni per pescare sfide senza ripetizioni
if "sfide_lei_giocate" not in st.session_state:
    st.session_state.sfide_lei_giocate = set()
if "sfide_lui_giocate" not in st.session_state:
    st.session_state.sfide_lui_giocate = set()

def pesca_sfida(chi: str):
    lista = sfide_per_lei if chi == "lei" else sfide_per_lui
    giocate = st.session_state.sfide_lei_giocate if chi == "lei" else st.session_state.sfide_lui_giocate

    if len(giocate) == len(lista):
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
