import time
import json

def get_choice(options):
    choice = input("> ").strip()
    if choice in options:
        return choice
    else:
        print("Ungültige Eingabe, bitte versuche es erneut.")
        return None

def save_game(state):
    with open("game_save.json", "w") as save_file:
        json.dump(state, save_file)
    print("Spiel gespeichert.")

def load_game():
    try:
        with open("game_save.json", "r") as save_file:
            return json.load(save_file)
    except FileNotFoundError:
        print("Kein gespeichertes Spiel gefunden.")
        return None

def start_game(state=None):
    if state is None:
        state = {"progress": "intro"}
    print("\nWillkommen zu 'Resistance: The Red Uprising'")
    time.sleep(1)
    print("Du bist Rick, ein junger Antifaschist in Deutschland im Jahr 2025.")
    time.sleep(1)
    print("Deine Mission: Kämpfe gegen den aufkommenden Faschismus und rette dein Land.")
    print("\n---\n")
    intro(state)

def intro(state):
    while True:
        print("Es ist ein düsterer Tag in deiner Heimatstadt. Die Rechte hat immer mehr Macht gewonnen, und du weißt, dass du handeln musst.")
        time.sleep(2)
        print("Deine Freunde haben dich kontaktiert. Sie wollen sich heute Abend treffen, um eine Protestaktion zu planen.")
        print("\nWas möchtest du tun?")
        print("1. Gehe zu dem Treffen.")
        print("2. Gehe nach Hause und denke darüber nach, was du tun solltest.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "meeting"
            meeting(state)
            break
        elif choice == "2":
            state["progress"] = "home"
            home(state)
            break

def home(state):
    while True:
        print("\n--- Zuhause ---")
        time.sleep(1)
        print("Du gehst nach Hause, setzt dich an deinen Schreibtisch und denkst nach. Was kannst du tun, um gegen die Rechten zu kämpfen?")
        time.sleep(2)
        print("Plötzlich klopft es an deiner Tür. Es ist dein Nachbar, ein Mitglied der rechten Bewegung. Er will mit dir reden.")
        print("\nWas möchtest du tun?")
        print("1. Öffne die Tür und höre ihm zu.")
        print("2. Ignoriere das Klopfen und bereite dich auf das Treffen am nächsten Tag vor.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "talk_to_neighbor"
            talk_to_neighbor(state)
            break
        elif choice == "2":
            state["progress"] = "prepare_for_meeting"
            prepare_for_meeting(state)
            break

def talk_to_neighbor(state):
    while True:
        print("\n--- Gespräch mit dem Nachbarn ---")
        time.sleep(1)
        print("Du öffnest die Tür und lässt deinen Nachbarn herein. Er beginnt, über die rechte Ideologie zu sprechen und versucht, dich zu überzeugen, dass er im Recht ist.")
        print("\nWas möchtest du tun?")
        print("1. Versuche, ihn zu überzeugen, dass die rechte Ideologie gefährlich ist.")
        print("2. Schlage die Tür zu und gehe zurück zu deinen Überlegungen.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "argue_with_neighbor"
            argue_with_neighbor(state)
            break
        elif choice == "2":
            state["progress"] = "ignore_neighbor"
            ignore_neighbor(state)
            break

def argue_with_neighbor(state):
    while True:
        print("\n--- Diskussion mit dem Nachbarn ---")
        time.sleep(1)
        print("Dein Nachbar beginnt mit rechter Propaganda:")
        print("'Die Zuwanderer nehmen uns die Jobs weg und zerstören unsere Kultur!'")
        
        print("\nWie möchtest du antworten?")
        print("1. 'Das stimmt nicht. Studien zeigen, dass Zuwanderung die Wirtschaft stärkt und unsere Gesellschaft vielfältiger macht.'")
        print("2. 'Das ist nur eine Ausrede, um Angst zu schüren. Die wahren Probleme liegen in der Ungleichheit und Korruption in unserem Land.'")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            print("\n--- Antwort ---")
            time.sleep(1)
            print("Du erklärst deinem Nachbarn, dass zahlreiche Studien belegen, dass Zuwanderer oft Jobs ausfüllen, die sonst unbesetzt bleiben würden, und dadurch zur wirtschaftlichen Stabilität beitragen.")
            next_argument(state)
            break
        elif choice == "2":
            print("\n--- Antwort ---")
            time.sleep(1)
            print("Du führst aus, dass die rechten Politiker die Ängste der Menschen ausnutzen, um von den echten Problemen abzulenken, wie der wachsenden Ungleichheit und Korruption.")
            next_argument(state)
            break

def next_argument(state):
    while True:
        print("\nDein Nachbar setzt seine Propaganda fort:")
        time.sleep(1)
        print("'Wir müssen die Kontrolle über unser Land zurückgewinnen. Diese Regierung hat uns verraten!'")
        
        print("\nWie möchtest du antworten?")
        print("1. 'Die Demokratie lebt vom Austausch und der Zusammenarbeit. Extreme Maßnahmen führen nur zu mehr Spaltung und Chaos.'")
        print("2. 'Es geht nicht darum, das Land zu kontrollieren, sondern darum, eine gerechte Gesellschaft für alle zu schaffen.'")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            print("\n--- Antwort ---")
            time.sleep(1)
            print("Du erklärst, dass eine stabile Demokratie auf Dialog und Kompromiss basiert. Extreme Maßnahmen führen zu Chaos und Gewalt, was die Situation nur verschlimmert.")
            convince_neighbor(state)
            break
        elif choice == "2":
            print("\n--- Antwort ---")
            time.sleep(1)
            print("Du argumentierst, dass die wahre Herausforderung darin besteht, eine Gesellschaft zu schaffen, die gerecht und inklusiv für alle ist, statt auf Angst und Kontrolle zu setzen.")
            convince_neighbor(state)
            break

def convince_neighbor(state):
    print("\n--- Überzeugung ---")
    time.sleep(1)
    print("Du schaffst es, deinen Nachbarn zum Nachdenken zu bringen. Er beginnt, an seiner Ideologie zu zweifeln.")
    print("Am nächsten Tag schließt er sich überraschenderweise eurer Gegendemonstration an und hilft, weitere Leute zu überzeugen.")
    print("\n--- Spiel Ende: Erfolg ---")
    time.sleep(1)
    print("Deine Entscheidung, mit Ruhe und Vernunft zu handeln, hat dazu geführt, dass die Bewegung wächst.")
    restart(state)

def ignore_neighbor(state):
    print("\n--- Ignoranz ---")
    time.sleep(1)
    print("Du schlägst die Tür zu und ignorierst deinen Nachbarn. Du verbringst den Rest des Abends damit, dich auf das Treffen vorzubereiten.")
    print("Doch am nächsten Tag erfährst du, dass dein Nachbar sich der rechten Miliz angeschlossen hat.")
    print("Er wird eine der treibenden Kräfte hinter der nächsten Aktion der Rechten sein.")
    print("\n--- Spiel Ende: Konsequenzen ---")
    time.sleep(1)
    print("Deine Entscheidung, nicht auf deinen Nachbarn einzugehen, hat zu einer Eskalation geführt.")
    restart(state)

def prepare_for_meeting(state):
    print("\n--- Vorbereitung ---")
    time.sleep(1)
    print("Du ignorierst das Klopfen und bereitest dich auf das Treffen am nächsten Tag vor.")
    print("Als du am nächsten Tag ankommst, ist die Gruppe bereits in Aktion. Du schließt dich ihnen an und bereitest eine große Protestaktion vor.")
    print("\n--- Spiel Ende: Vorbereitung ---")
    time.sleep(1)
    print("Deine Entscheidung, dich zu konzentrieren und vorzubereiten, hat dir geholfen, dich besser zu organisieren. Der Kampf geht weiter.")
    restart(state)

def meeting(state):
    while True:
        print("\n--- Treffen ---")
        time.sleep(1)
        print("Du betrittst einen kleinen, verlassenen Lagerraum. Ein paar Dutzend Leute haben sich hier versammelt, alle entschlossen, gegen die Rechte zu kämpfen.")
        print("Der Anführer der Gruppe, Anna, begrüßt dich. 'Wir müssen handeln', sagt sie. 'Die Rechte plant morgen eine große Kundgebung in der Stadt. Wir können das nicht zulassen.'")
        print("\nWas möchtest du tun?")
        print("1. Schlage vor, eine friedliche Gegendemonstration zu organisieren.")
        print("2. Schlage vor, die Kundgebung der Rechten zu sabotieren.")
        print("3. Schlage vor, die Öffentlichkeit durch Medienarbeit und soziale Netzwerke zu mobilisieren.")
        
        choice = get_choice(["1", "2", "3"])
        if choice == "1":
            state["progress"] = "peaceful_protest"
            peaceful_protest(state)
            break
        elif choice == "2":
            state["progress"] = "sabotage"
            sabotage(state)
            break
        elif choice == "3":
            state["progress"] = "media_campaign"
            media_campaign(state)
            break

def peaceful_protest(state):
    while True:
        print("\n--- Friedliche Gegendemonstration ---")
        time.sleep(1)
        print("Du schlägst vor, eine friedliche Gegendemonstration zu organisieren. Die Gruppe stimmt zu.")
        print("Am nächsten Tag versammeln sich Hunderte von Menschen in der Stadt. Es ist eine kraftvolle, aber friedliche Demonstration.")
        print("Die Rechte reagiert mit Gewalt, aber eure Botschaft wird in den Medien weit verbreitet. Viele Menschen beginnen, die Bewegung zu unterstützen.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Versuche, mit der Mitte zu verhandeln, um mehr Unterstützung zu erhalten.")
        print("2. Plane eine weitere, größere Demonstration in der Hauptstadt.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "negotiate_with_center"
            negotiate_with_center(state)
            break
        elif choice == "2":
            state["progress"] = "larger_protest"
            larger_protest(state)
            break

def sabotage(state):
    while True:
        print("\n--- Sabotage ---")
        time.sleep(1)
        print("Du schlägst vor, die Kundgebung der Rechten zu sabotieren. Die Gruppe ist sich unsicher, aber schließlich stimmen sie zu.")
        print("In der Nacht dringt ihr in das Lagerhaus ein, wo die Rechten ihre Ausrüstung aufbewahren. Ihr zerstört alles, was ihr finden könnt.")
        print("Am nächsten Tag ist die Kundgebung ein Desaster. Doch die Rechten machen Jagd auf die Verantwortlichen.")
        print("Eure Aktion hat sie nur noch wütender gemacht, und die Gewalt eskaliert weiter.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Verstecke dich und plane deinen nächsten Schritt.")
        print("2. Stelle dich der Rechten und versuche, ihre Pläne öffentlich zu entlarven.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "hide_and_plan"
            hide_and_plan(state)
            break
        elif choice == "2":
            state["progress"] = "expose_right"
            expose_right(state)
            break

def media_campaign(state):
    while True:
        print("\n--- Medienkampagne ---")
        time.sleep(1)
        print("Du schlägst vor, eine Medienkampagne zu starten, um die Öffentlichkeit zu mobilisieren.")
        print("Die Gruppe stimmt zu, und ihr beginnt, eure Botschaft über soziale Netzwerke und unabhängige Medien zu verbreiten.")
        print("Die Kampagne wird viral, und immer mehr Menschen beginnen, sich der Bewegung anzuschließen.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Versuche, durch Crowdfunding Gelder für eure Aktionen zu sammeln.")
        print("2. Organisiere eine Online-Debatte mit einem prominenten Vertreter der Rechten.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "crowdfunding"
            crowdfunding(state)
            break
        elif choice == "2":
            state["progress"] = "online_debate"
            online_debate(state)
            break

def negotiate_with_center(state):
    while True:
        print("\n--- Verhandlungen mit der Mitte ---")
        time.sleep(1)
        print("Du triffst dich mit Vertretern der Mitte, um sie davon zu überzeugen, eure Bewegung zu unterstützen.")
        print("Sie sind vorsichtig, aber sie sehen die Notwendigkeit, gemeinsam gegen die Rechte vorzugehen.")
        print("Nach langen Diskussionen erklären sie sich bereit, eine gemeinsame Erklärung gegen die rechte Gewalt abzugeben.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Suche nach weiteren potenziellen Verbündeten, um die Allianz zu erweitern.")
        print("2. Organisiere eine groß angelegte Kampagne, um die Mitte stärker in die Bewegung einzubinden.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "recruit_allies"
            recruit_allies(state)
            break
        elif choice == "2":
            state["progress"] = "middle_campaign"
            middle_campaign(state)
            break

def crowdfunding(state):
    while True:
        print("\n--- Crowdfunding ---")
        time.sleep(1)
        print("Du startest eine Crowdfunding-Kampagne, um Gelder für eure Aktionen zu sammeln.")
        print("Die Kampagne ist ein Erfolg, und ihr habt nun die Mittel, um größere Aktionen zu planen.")
        print("Mit den neuen Ressourcen beginnt ihr, professioneller zu arbeiten und größere Aktionen zu organisieren.")
        print("\nWie möchtest du die Gelder verwenden?")
        print("1. Finanziere friedliche Demonstrationen und Aufklärungskampagnen.")
        print("2. Investiere in verdeckte Operationen, um die rechte Bewegung zu unterminieren.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "fund_peaceful_protests"
            fund_peaceful_protests(state)
            break
        elif choice == "2":
            state["progress"] = "fund_covert_operations"
            fund_covert_operations(state)
            break

def recruit_allies(state):
    while True:
        print("\n--- Neue Verbündete ---")
        time.sleep(1)
        print("Du beginnst, weitere potenzielle Verbündete aus verschiedenen politischen und sozialen Gruppen zu rekrutieren.")
        print("Dabei stößt du auf verschiedene Herausforderungen und Konflikte.")
        print("\nWie möchtest du vorgehen?")
        print("1. Versuche, zwischen den unterschiedlichen Gruppen zu vermitteln.")
        print("2. Konzentriere dich auf die stärksten Gruppen und lass die schwächeren beiseite.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "mediate_groups"
            mediate_groups(state)
            break
        elif choice == "2":
            state["progress"] = "focus_on_strong_groups"
            focus_on_strong_groups(state)
            break

def middle_campaign(state):
    while True:
        print("\n--- Kampagne ---")
        time.sleep(1)
        print("Du organisierst eine groß angelegte Kampagne, um die Mitte stärker in die Bewegung einzubinden.")
        print("Die Kampagne ist erfolgreich, und immer mehr Menschen schließen sich der Bewegung an.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Nutze die Dynamik, um eine nationale Bewegung zu starten.")
        print("2. Setze auf lokale Aktionen, um die Unterstützung weiter zu festigen.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "national_movement"
            national_movement(state)
            break
        elif choice == "2":
            state["progress"] = "local_actions"
            local_actions(state)
            break

def local_actions(state):
    print("\n--- Lokale Aktionen ---")
    time.sleep(1)
    print("Du entscheidest dich, lokale Aktionen zu organisieren, um die Unterstützung auf Gemeindeebene zu festigen.")
    print("Durch kleinere, gezielte Aktionen in verschiedenen Regionen schaffst du es, eine breite Basis an Unterstützern aufzubauen.")
    print("\nDie rechte Bewegung versucht, eure Bemühungen zu untergraben, aber die starke lokale Verankerung eurer Bewegung macht es schwer, euch zu stoppen.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Baue ein Netzwerk lokaler Gruppen auf, um die Bewegung noch weiter zu verbreiten.")
    print("2. Organisiere eine Serie von Kooperationsprojekten mit anderen sozialen Bewegungen, um eure Basis zu erweitern.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "build_local_network"
        build_local_network(state)
    elif choice == "2":
        state["progress"] = "cooperate_with_movements"
        cooperate_with_movements(state)

def build_local_network(state):
    print("\n--- Lokales Netzwerk ---")
    time.sleep(1)
    print("Du konzentrierst dich darauf, ein starkes Netzwerk lokaler Gruppen aufzubauen.")
    print("Diese Gruppen arbeiten eng zusammen, tauschen Informationen aus und koordinieren ihre Aktionen.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Organisiere ein landesweites Treffen der lokalen Gruppen, um die Koordination zu verbessern.")
    print("2. Entwickle gemeinsame Aktionspläne, um die Schlagkraft des Netzwerks zu erhöhen.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "national_meeting"
        national_meeting(state)
    elif choice == "2":
        state["progress"] = "joint_action_plans"
        joint_action_plans(state)

def fund_peaceful_protests(state):
    while True:
        print("\n--- Friedliche Proteste ---")
        time.sleep(1)
        print("Du entscheidest dich, die Gelder in friedliche Demonstrationen und Aufklärungskampagnen zu investieren.")
        print("Dies stärkt das öffentliche Bild der Bewegung und zieht weitere Unterstützer an.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Organisiere eine große Demonstration in der Hauptstadt, um den Erfolg zu zeigen.")
        print("2. Nutze die Mittel, um Bildungsprogramme zu fördern, die über die Gefahr der rechten Ideologie aufklären.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "larger_protest"
            larger_protest(state)
            break
        elif choice == "2":
            state["progress"] = "education_programs"
            education_programs(state)
            break

def information_campaign(state):
    print("\n--- Informationskampagne ---")
    time.sleep(1)
    print("Du entscheidest dich, eine Kampagne zu starten, um die Rechte durch gezielte Informationsverbreitung zu diskreditieren.")
    print("Die Kampagne gewinnt an Fahrt, und immer mehr Menschen erkennen die wahren Absichten der rechten Bewegung.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Setze auf eine breite Medienkampagne, um die Bewegung weiter zu schwächen.")
    print("2. Fokussiere dich auf gezielte Angriffe auf Schlüsselpersonen der rechten Bewegung.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "media_campaign"
        media_campaign_cooperation(state)
    elif choice == "2":
        state["progress"] = "target_key_figures"
        target_key_figures(state)

def nationwide_campaign(state):
    print("\n--- Landesweite Kampagne ---")
    time.sleep(1)
    print("Du startest eine landesweite Kampagne, die in jeder großen Stadt gleichzeitig stattfindet.")
    print("Die Bewegung wächst schnell und gewinnt an Stärke.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Nutze die nationale Präsenz, um Druck auf die Regierung auszuüben.")
    print("2. Organisiere landesweite Streiks, um die rechte Bewegung weiter zu destabilisieren.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "government_pressure"
        government_pressure(state)
    elif choice == "2":
        state["progress"] = "national_strikes"
        national_strikes(state)        

def develop_safety_strategies(state):
    print("\n--- Sicherheitsstrategien entwickeln ---")
    time.sleep(1)
    print("Du arbeitest daran, umfassende Sicherheitsstrategien für die Bewegung zu entwickeln.")
    print("Diese Strategien schützen die Mitglieder der Bewegung und ermöglichen es ihnen, effektiv zu handeln.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Setze auf den Aufbau sicherer Kommunikationskanäle.")
    print("2. Entwickle Notfallpläne für mögliche Angriffe der rechten Bewegung.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "secure_communications"
        secure_communications(state)
    elif choice == "2":
        state["progress"] = "emergency_plans"
        emergency_plans(state)

def coordinated_actions(state):
    print("\n--- Koordinierte Aktionen ---")
    time.sleep(1)
    print("Du organisierst koordinierte Aktionen in mehreren Städten gleichzeitig.")
    print("Diese Aktionen führen zu einer Welle der Unterstützung in der Bevölkerung.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Plane weitere koordinierte Aktionen, um die Bewegung weiter zu stärken.")
    print("2. Konzentriere dich darauf, die erzielten Erfolge zu konsolidieren.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "more_coordinated_actions"
        more_coordinated_actions(state)
    elif choice == "2":
        state["progress"] = "consolidate_success"
        consolidate_success(state)

def fund_covert_operations(state):
    while True:
        print("\n--- Verdeckte Operationen ---")
        time.sleep(1)
        print("Du entscheidest dich, die Gelder in verdeckte Operationen zu investieren, um die rechte Bewegung zu unterminieren.")
        print("Diese Strategie ist riskant, führt aber zu bedeutenden Erfolgen gegen die rechte Führung.")
        print("\nWie möchtest du die Operationen fortführen?")
        print("1. Fokussiere dich auf die Sabotage ihrer Kommunikationsmittel.")
        print("2. Setze auf Angriffe auf die finanziellen Unterstützer der rechten Bewegung.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "sabotage_communications"
            sabotage_communications(state)
            break
        elif choice == "2":
            state["progress"] = "attack_financial_backers"
            attack_financial_backers(state)
            break

def hide_and_plan(state):
    print("\n--- Verstecken und Planen ---")
    time.sleep(1)
    print("Du und deine Gruppe versteckt euch, um dem Zorn der Rechten zu entgehen.")
    print("Während ihr euch versteckt, plant ihr eure nächsten Schritte sorgfältig.")
    print("Ihr entscheidet euch, die rechte Bewegung durch gezielte Aktionen zu schwächen.")
    print("\nWie möchtest du vorgehen?")
    print("1. Plane einen Angriff auf die Führung der rechten Bewegung.")
    print("2. Fokussiere dich auf die Verbreitung von Informationen, um die Rechte zu diskreditieren.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "attack_leadership"
        attack_leadership(state)
    elif choice == "2":
        state["progress"] = "information_campaign"
        information_campaign(state)

def expose_right(state):
    print("\n--- Enthüllung ---")
    time.sleep(1)
    print("Du stellst dich der Rechten und versuchst, ihre Pläne öffentlich zu entlarven.")
    print("Du organisierst eine Pressekonferenz und legst Beweise für ihre illegalen Aktivitäten vor.")
    print("Die Enthüllungen schlagen hohe Wellen, aber die Rechte schlägt hart zurück.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Setze die Enthüllungen fort und bringe weitere Informationen an die Öffentlichkeit.")
    print("2. Konzentriere dich darauf, die Bewegung zu schützen und das Risiko zu minimieren.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "continue_exposure"
        continue_exposure(state)
    elif choice == "2":
        state["progress"] = "risk_management"
        risk_management(state)

def online_debate(state):
    while True:
        print("\n--- Online-Debatte ---")
        time.sleep(1)
        print("Du organisierst eine Online-Debatte mit einem prominenten Vertreter der Rechten.")
        print("Die Debatte wird live gestreamt und zieht ein großes Publikum an.")
        print("Du bereitest dich gut vor und widerlegst seine Argumente souverän.")
        print("Die Öffentlichkeit beginnt, die rechte Ideologie in Frage zu stellen.")
        print("\nWie möchtest du die Debatte nutzen?")
        print("1. Lade weitere prominente Vertreter ein, um die Diskussion zu erweitern.")
        print("2. Nutze die Debatte, um eine Petition zu starten und politische Maßnahmen zu fordern.")
        
        choice = get_choice(["1", "2"])
        if choice == "1":
            state["progress"] = "expand_debate"
            expand_debate(state)
            break
        elif choice == "2":
            state["progress"] = "start_petition"
            start_petition(state)
            break

def mediate_groups(state):
    print("\n--- Vermittlung ---")
    time.sleep(1)
    print("Du entscheidest dich, zwischen den unterschiedlichen Gruppen zu vermitteln, um eine breite Allianz zu schmieden.")
    print("Nach harten Verhandlungen gelingt es dir, eine starke Koalition zu bilden.")
    print("\nWie möchtest du die Allianz nutzen?")
    print("1. Startet eine landesweite Kampagne, um den Widerstand zu verbreiten.")
    print("2. Nutzt die Allianz, um die rechte Bewegung direkt anzugreifen.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "nationwide_campaign"
        nationwide_campaign(state)
    elif choice == "2":
        state["progress"] = "direct_attack"
        direct_attack(state)

def focus_on_strong_groups(state):
    print("\n--- Fokussierung ---")
    time.sleep(1)
    print("Du konzentrierst dich auf die stärksten Gruppen, um eine effektive Widerstandsbewegung zu bilden.")
    print("Dies führt jedoch zu Spannungen mit den schwächeren Gruppen, die sich ausgeschlossen fühlen.")
    print("\nWie möchtest du weitermachen?")
    print("1. Versuche, die Spannungen mit den schwächeren Gruppen zu lösen.")
    print("2. Ignoriere die Spannungen und setze auf eine starke, aber kleine Gruppe.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "resolve_tensions"
        resolve_tensions(state)
    elif choice == "2":
        state["progress"] = "small_strong_group"
        small_strong_group(state)

def larger_protest(state):
    print("\n--- Große Demonstration ---")
    time.sleep(1)
    print("Du organisierst eine große Demonstration in der Hauptstadt, um die Aufmerksamkeit auf eure Sache zu lenken.")
    print("Die Demonstration zieht Tausende von Teilnehmern an und wird in den Medien stark beachtet.")
    print("\n--- Spiel Ende: Demonstration ---")
    time.sleep(1)
    print("Deine Entscheidung, die Bewegung in die Hauptstadt zu bringen, hat eure Botschaft verbreitet und die Unterstützung für den Widerstand gestärkt.")
    restart(state)

def education_programs(state):
    print("\n--- Bildungsprogramme ---")
    time.sleep(1)
    print("Du entscheidest dich, die Mittel zu nutzen, um Bildungsprogramme zu fördern, die über die Gefahren der rechten Ideologie aufklären.")
    print("Diese Programme erreichen eine breite Zielgruppe und tragen dazu bei, die öffentliche Meinung zu verändern.")
    print("\n--- Spiel Ende: Aufklärung ---")
    time.sleep(1)
    print("Dank deiner Entscheidung, in Bildung zu investieren, wächst das Bewusstsein für die Probleme, die durch die rechte Ideologie verursacht werden.")
    restart(state)

def sabotage_communications(state):
    print("\n--- Kommunikationssabotage ---")
    time.sleep(1)
    print("Du entscheidest dich, die Kommunikationsmittel der rechten Bewegung zu sabotieren.")
    print("Diese Aktion stört ihre Organisation erheblich und schwächt ihre Fähigkeit, schnell zu reagieren.")
    print("\n--- Spiel Ende: Sabotage Erfolg ---")
    time.sleep(1)
    print("Deine Entscheidung, ihre Kommunikationswege zu unterbrechen, hat die rechte Bewegung entscheidend geschwächt.")
    restart(state)

def attack_financial_backers(state):
    print("\n--- Angriff auf finanzielle Unterstützer ---")
    time.sleep(1)
    print("Du richtest deine Angriffe auf die finanziellen Unterstützer der rechten Bewegung.")
    print("Diese Aktion destabilisiert ihre Finanzierung und zwingt sie, ihre Aktivitäten zu reduzieren.")
    print("\n--- Spiel Ende: Finanzielle Sabotage ---")
    time.sleep(1)
    print("Durch den Erfolg deiner Angriffe auf ihre Finanzen wurde die rechte Bewegung erheblich geschwächt.")
    restart(state)

def attack_leadership(state):
    while True:
        print("\n--- Angriff auf die Führung ---")
        time.sleep(1)
        print("Du planst einen gezielten Angriff auf die Führung der rechten Bewegung.")
        print("Dies schwächt ihre Organisation erheblich, aber es führt auch zu erhöhter Gewaltbereitschaft auf ihrer Seite.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Setze weitere Angriffe auf die Führung fort.")
        print("2. Ziehe dich zurück und beobachte die Reaktion der Rechten.")

        choice = get_choice(["1", "2"])
        if choice == "1":
            print("\n--- Fortgesetzte Angriffe ---")
            time.sleep(1)
            print("Du setzt deine Angriffe fort und schwächst die rechte Bewegung weiter.")
            print("Allerdings eskaliert die Gewalt zunehmend, und es kommt zu offenen Kämpfen auf den Straßen.")
            print("Die Bewegung steht nun am Rand eines Bürgerkriegs.")
            restart(state)
            break
        elif choice == "2":
            print("\n--- Rückzug und Beobachtung ---")
            time.sleep(1)
            print("Du ziehst dich zurück und beobachtest die Reaktionen.")
            print("Die rechte Bewegung erholt sich langsam, aber die Führung ist geschwächt und kann nicht sofort zurückschlagen.")
            restart(state)
            break

def continue_exposure(state):
    while True:
        print("\n--- Fortsetzung der Enthüllungen ---")
        time.sleep(1)
        print("Du entscheidest dich, weitere Informationen über die rechte Bewegung öffentlich zu machen.")
        print("Dies führt zu wachsendem Druck auf die rechte Führung, aber auch zu verstärkten Gegenmaßnahmen.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Veröffentliche alle gesammelten Informationen auf einmal.")
        print("2. Veröffentliche die Informationen schrittweise, um den Druck über einen längeren Zeitraum aufrechtzuerhalten.")

        choice = get_choice(["1", "2"])
        if choice == "1":
            print("\n--- Veröffentlichung aller Informationen ---")
            time.sleep(1)
            print("Du veröffentlichst alle gesammelten Informationen auf einmal.")
            print("Die Enthüllungen führen zu einem großen öffentlichen Aufschrei, aber auch zu einer gefährlichen Gegenreaktion.")
            restart(state)
            break
        elif choice == "2":
            print("\n--- Schrittweise Veröffentlichung ---")
            time.sleep(1)
            print("Du entscheidest dich, die Informationen schrittweise zu veröffentlichen.")
            print("Dies hält den Druck auf die rechte Bewegung über einen längeren Zeitraum aufrecht und führt zu internen Spannungen in ihren Reihen.")
            restart(state)
            break

def risk_management(state):
    print("\n--- Risikomanagement ---")
    time.sleep(1)
    print("Du entscheidest dich, die Bewegung zu schützen und das Risiko zu minimieren.")
    print("Dadurch handelst du vorsichtiger, aber es erlaubt dir, die Bewegung langfristig stabil zu halten.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Baue sichere Kommunikationskanäle auf, um die Bewegung zu koordinieren.")
    print("2. Entwickle Strategien, um die Sicherheit der Mitglieder zu gewährleisten.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "secure_communications"
        secure_communications(state)
    elif choice == "2":
        state["progress"] = "develop_safety_strategies"
        develop_safety_strategies(state)

def secure_communications(state):
    print("\n--- Sichere Kommunikationskanäle ---")
    time.sleep(1)
    print("Du beginnst, sichere Kommunikationskanäle für die Bewegung aufzubauen.")
    print("Diese Kanäle helfen, die Koordination und Planung der Aktionen zu verbessern und vor Überwachung zu schützen.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Nutze die Kommunikationskanäle, um koordinierte Aktionen in mehreren Städten gleichzeitig zu starten.")
    print("2. Verstärke die Sicherheit der Kanäle weiter, um zukünftige Angriffe zu verhindern.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "coordinated_actions"
        coordinated_actions(state)
    elif choice == "2":
        state["progress"] = "enhance_security"
        enhance_security(state)

def enhance_security(state):
    print("\n--- Sicherheit verstärken ---")
    time.sleep(1)
    print("Du entscheidest dich, die Sicherheitsmaßnahmen der Bewegung weiter zu verstärken.")
    print("Diese Maßnahmen schützen die Bewegung vor Überwachung und Angriffen.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Setze auf den Schutz der Kommunikationskanäle.")
    print("2. Entwickle Strategien, um die Identitäten der Mitglieder zu verschleiern.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "protect_communications"
        protect_communications(state)
    elif choice == "2":
        state["progress"] = "conceal_identities"
        conceal_identities(state)
        
def coordinated_actions(state):
    print("\n--- Koordinierte Aktionen ---")
    time.sleep(1)
    print("Du organisierst koordinierte Aktionen in mehreren Städten gleichzeitig.")
    print("Diese Aktionen führen zu einer Welle der Unterstützung in der Bevölkerung.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Plane weitere koordinierte Aktionen, um die Bewegung weiter zu stärken.")
    print("2. Konzentriere dich darauf, die erzielten Erfolge zu konsolidieren.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "more_coordinated_actions"
        more_coordinated_actions(state)
    elif choice == "2":
        state["progress"] = "consolidate_success"
        consolidate_success(state)

def expand_debate(state):
    print("\n--- Erweiterte Debatte ---")
    time.sleep(1)
    print("Du lädst weitere prominente Vertreter ein, um die Diskussion zu erweitern.")
    print("Die Debatte erreicht ein noch größeres Publikum und gewinnt an Tiefe und Einfluss.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Organisiere eine Serie von Debatten, um die Öffentlichkeit weiter zu sensibilisieren.")
    print("2. Nutze die Debatte, um konkrete politische Forderungen zu stellen.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "debate_series"
        debate_series(state)
    elif choice == "2":
        state["progress"] = "political_demands"
        political_demands(state)

def debate_series(state):
    print("\n--- Debattenreihe ---")
    time.sleep(1)
    print("Du organisierst eine Serie von Debatten, um die Öffentlichkeit weiter zu sensibilisieren.")
    print("Diese Debatten ziehen große Aufmerksamkeit auf sich und führen zu einer wachsenden Unterstützung für eure Bewegung.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Fokussiere die Debatten auf politische Forderungen.")
    print("2. Lade weitere prominente Redner ein, um die Diskussionen zu erweitern.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "political_demands"
        political_demands(state)
    elif choice == "2":
        state["progress"] = "invite_speakers"
        invite_speakers(state)

def start_petition(state):
    print("\n--- Petition ---")
    time.sleep(1)
    print("Du nutzt die Debatte, um eine Petition zu starten und politische Maßnahmen zu fordern.")
    print("Die Petition gewinnt schnell an Unterstützung und übt Druck auf die Regierung aus.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Verwende die Unterschriften, um einen direkten Dialog mit der Regierung zu erzwingen.")
    print("2. Organisiere eine Massenkundgebung, um die Unterstützung für die Petition zu demonstrieren.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "dialog_with_government"
        dialog_with_government(state)
    elif choice == "2":
        state["progress"] = "mass_rally"
        mass_rally(state)

def direct_attack(state):
    print("\n--- Direkter Angriff ---")
    time.sleep(1)
    print("Du entscheidest dich, die rechte Bewegung direkt anzugreifen, indem du ihre wichtigsten Mitglieder und Infrastrukturen ins Visier nimmst.")
    print("Dies führt zu massiven Unruhen und einer Eskalation des Konflikts.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Führe weitere Angriffe durch, um die Rechten zu destabilisieren.")
    print("2. Nutze die Unruhen, um eine breite Mobilisierung der Bevölkerung zu erreichen.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "more_attacks"
        more_attacks(state)
    elif choice == "2":
        state["progress"] = "mobilize_population"
        mobilize_population(state)

def resolve_tensions(state):
    print("\n--- Spannungen lösen ---")
    time.sleep(1)
    print("Du arbeitest hart daran, die Spannungen zwischen den verschiedenen Gruppen in deiner Allianz zu lösen.")
    print("Durch geschickte Verhandlungen und Kompromisse schaffst du es, die Einheit zu bewahren.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Führe regelmäßige Treffen durch, um den Zusammenhalt der Allianz zu stärken.")
    print("2. Entwickle gemeinsame Ziele und Strategien, um die Allianz zu festigen.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "regular_meetings"
        regular_meetings(state)
    elif choice == "2":
        state["progress"] = "common_goals"
        common_goals(state)

def small_strong_group(state):
    print("\n--- Kleine, starke Gruppe ---")
    time.sleep(1)
    print("Du entscheidest dich, dich auf eine kleine, aber starke Gruppe zu konzentrieren.")
    print("Diese Gruppe ist hocheffizient, aber die fehlende breite Unterstützung macht sie anfälliger für Gegenangriffe.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Rekrutiere gezielt neue Mitglieder, um die Gruppe zu verstärken.")
    print("2. Entwickle spezialisierte Taktiken, um die Effektivität der kleinen Gruppe zu maximieren.")
    
    choice = get_choice(["1", "2"])
    if choice == "1":
        state["progress"] = "recruit_more_members"
        recruit_more_members(state)
    elif choice == "2":
        state["progress"] = "special_tactics"
        special_tactics(state)

def restart(state):
    while True:
        print("\nMöchtest du das Spiel speichern oder erneut spielen? (speichern/ja/nein)")
        choice = input("> ").strip().lower()

        if choice == "speichern":
            save_game(state)
            print("Spiel gespeichert. Möchtest du es fortsetzen? (ja/nein)")
            continue_game = input("> ").strip().lower()
            if continue_game == "ja":
                start_game(state)
            else:
                print("Danke fürs Spielen!")
            break
        elif choice == "ja":
            start_game()
            break
        elif choice == "nein":
            print("Danke fürs Spielen!")
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

# Spiel starten
start_game()
