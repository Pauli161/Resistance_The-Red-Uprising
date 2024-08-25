test

def start_game():
    print("Willkommen zu 'Resistance: The Red Uprising'")
    print("Du bist Rick, ein junger Antifaschist in Deutschland im Jahr 2025.")
    print("Deine Mission: Kämpfe gegen den aufkommenden Faschismus und rette dein Land.")
    print("\n---\n")
    intro()

def intro():
    while True:
        print("Es ist ein düsterer Tag in deiner Heimatstadt. Die Rechte hat immer mehr Macht gewonnen, und du weißt, dass du handeln musst.")
        print("Deine Freunde haben dich kontaktiert. Sie wollen sich heute Abend treffen, um eine Protestaktion zu planen.")
        print("\nWas möchtest du tun?")
        print("1. Gehe zu dem Treffen.")
        print("2. Gehe nach Hause und denke darüber nach, was du tun solltest.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            meeting()
            break
        elif choice == "2":
            home()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def home():
    while True:
        print("\n--- Zuhause ---")
        print("Du gehst nach Hause, setzt dich an deinen Schreibtisch und denkst nach. Was kannst du tun, um gegen die Rechten zu kämpfen?")
        print("Plötzlich klopft es an deiner Tür. Es ist dein Nachbar, ein Mitglied der rechten Bewegung. Er will mit dir reden.")
        print("\nWas möchtest du tun?")
        print("1. Öffne die Tür und höre ihm zu.")
        print("2. Ignoriere das Klopfen und bereite dich auf das Treffen am nächsten Tag vor.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            talk_to_neighbor()
            break
        elif choice == "2":
            prepare_for_meeting()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def talk_to_neighbor():
    while True:
        print("\n--- Gespräch mit dem Nachbarn ---")
        print("Du öffnest die Tür und lässt deinen Nachbarn herein. Er beginnt, über die rechte Ideologie zu sprechen und versucht, dich zu überzeugen, dass er im Recht ist.")
        print("\nWas möchtest du tun?")
        print("1. Versuche, ihn zu überzeugen, dass die rechte Ideologie gefährlich ist.")
        print("2. Schlage die Tür zu und gehe zurück zu deinen Überlegungen.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            argue_with_neighbor()
            break
        elif choice == "2":
            ignore_neighbor()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def argue_with_neighbor():
    while True:
        print("\n--- Diskussion mit dem Nachbarn ---")
        print("Dein Nachbar beginnt mit rechter Propaganda:")
        print("'Die Zuwanderer nehmen uns die Jobs weg und zerstören unsere Kultur!'")
        
        print("\nWie möchtest du antworten?")
        print("1. 'Das stimmt nicht. Studien zeigen, dass Zuwanderung die Wirtschaft stärkt und unsere Gesellschaft vielfältiger macht.'")
        print("2. 'Das ist nur eine Ausrede, um Angst zu schüren. Die wahren Probleme liegen in der Ungleichheit und Korruption in unserem Land.'")
        
        choice = input("> ").strip()
        
        if choice == "1":
            print("\n--- Antwort ---")
            print("Du erklärst deinem Nachbarn, dass zahlreiche Studien belegen, dass Zuwanderer oft Jobs ausfüllen, die sonst unbesetzt bleiben würden, und dadurch zur wirtschaftlichen Stabilität beitragen.")
            next_argument()
            break
        elif choice == "2":
            print("\n--- Antwort ---")
            print("Du führst aus, dass die rechten Politiker die Ängste der Menschen ausnutzen, um von den echten Problemen abzulenken, wie der wachsenden Ungleichheit und Korruption.")
            next_argument()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def next_argument():
    while True:
        print("\nDein Nachbar setzt seine Propaganda fort:")
        print("'Wir müssen die Kontrolle über unser Land zurückgewinnen. Diese Regierung hat uns verraten!'")
        
        print("\nWie möchtest du antworten?")
        print("1. 'Die Demokratie lebt vom Austausch und der Zusammenarbeit. Extreme Maßnahmen führen nur zu mehr Spaltung und Chaos.'")
        print("2. 'Es geht nicht darum, das Land zu kontrollieren, sondern darum, eine gerechte Gesellschaft für alle zu schaffen.'")
        
        choice = input("> ").strip()
        
        if choice == "1":
            print("\n--- Antwort ---")
            print("Du erklärst, dass eine stabile Demokratie auf Dialog und Kompromiss basiert. Extreme Maßnahmen führen zu Chaos und Gewalt, was die Situation nur verschlimmert.")
            convince_neighbor()
            break
        elif choice == "2":
            print("\n--- Antwort ---")
            print("Du argumentierst, dass die wahre Herausforderung darin besteht, eine Gesellschaft zu schaffen, die gerecht und inklusiv für alle ist, statt auf Angst und Kontrolle zu setzen.")
            convince_neighbor()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def convince_neighbor():
    print("\n--- Überzeugung ---")
    print("Du schaffst es, deinen Nachbarn zum Nachdenken zu bringen. Er beginnt, an seiner Ideologie zu zweifeln.")
    print("Am nächsten Tag schließt er sich überraschenderweise eurer Gegendemonstration an und hilft, weitere Leute zu überzeugen.")
    print("\n--- Spiel Ende: Erfolg ---")
    print("Deine Entscheidung, mit Ruhe und Vernunft zu handeln, hat dazu geführt, dass die Bewegung wächst.")
    restart()

def ignore_neighbor():
    print("\n--- Ignoranz ---")
    print("Du schlägst die Tür zu und ignorierst deinen Nachbarn. Du verbringst den Rest des Abends damit, dich auf das Treffen vorzubereiten.")
    print("Doch am nächsten Tag erfährst du, dass dein Nachbar sich der rechten Miliz angeschlossen hat.")
    print("Er wird eine der treibenden Kräfte hinter der nächsten Aktion der Rechten sein.")
    print("\n--- Spiel Ende: Konsequenzen ---")
    print("Deine Entscheidung, nicht auf deinen Nachbarn einzugehen, hat zu einer Eskalation geführt.")
    restart()

def prepare_for_meeting():
    print("\n--- Vorbereitung ---")
    print("Du ignorierst das Klopfen und bereitest dich auf das Treffen am nächsten Tag vor.")
    print("Als du am nächsten Tag ankommst, ist die Gruppe bereits in Aktion. Du schließt dich ihnen an und bereitest eine große Protestaktion vor.")
    print("\n--- Spiel Ende: Vorbereitung ---")
    print("Deine Entscheidung, dich zu konzentrieren und vorzubereiten, hat dir geholfen, dich besser zu organisieren. Der Kampf geht weiter.")
    restart()

def meeting():
    while True:
        print("\n--- Treffen ---")
        print("Du betrittst einen kleinen, verlassenen Lagerraum. Ein paar Dutzend Leute haben sich hier versammelt, alle entschlossen, gegen die Rechte zu kämpfen.")
        print("Der Anführer der Gruppe, Anna, begrüßt dich. 'Wir müssen handeln', sagt sie. 'Die Rechte plant morgen eine große Kundgebung in der Stadt. Wir können das nicht zulassen.'")
        print("\nWas möchtest du tun?")
        print("1. Schlage vor, eine friedliche Gegendemonstration zu organisieren.")
        print("2. Schlage vor, die Kundgebung der Rechten zu sabotieren.")
        print("3. Schlage vor, die Öffentlichkeit durch Medienarbeit und soziale Netzwerke zu mobilisieren.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            peaceful_protest()
            break
        elif choice == "2":
            sabotage()
            break
        elif choice == "3":
            media_campaign()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def peaceful_protest():
    while True:
        print("\n--- Friedliche Gegendemonstration ---")
        print("Du schlägst vor, eine friedliche Gegendemonstration zu organisieren. Die Gruppe stimmt zu.")
        print("Am nächsten Tag versammeln sich Hunderte von Menschen in der Stadt. Es ist eine kraftvolle, aber friedliche Demonstration.")
        print("Die Rechte reagiert mit Gewalt, aber eure Botschaft wird in den Medien weit verbreitet. Viele Menschen beginnen, die Bewegung zu unterstützen.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Versuche, mit der Mitte zu verhandeln, um mehr Unterstützung zu erhalten.")
        print("2. Plane eine weitere, größere Demonstration in der Hauptstadt.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            negotiate_with_center()
            break
        elif choice == "2":
            larger_protest()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def sabotage():
    while True:
        print("\n--- Sabotage ---")
        print("Du schlägst vor, die Kundgebung der Rechten zu sabotieren. Die Gruppe ist sich unsicher, aber schließlich stimmen sie zu.")
        print("In der Nacht dringt ihr in das Lagerhaus ein, wo die Rechten ihre Ausrüstung aufbewahren. Ihr zerstört alles, was ihr finden könnt.")
        print("Am nächsten Tag ist die Kundgebung ein Desaster. Doch die Rechten machen Jagd auf die Verantwortlichen.")
        print("Eure Aktion hat sie nur noch wütender gemacht, und die Gewalt eskaliert weiter.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Verstecke dich und plane deinen nächsten Schritt.")
        print("2. Stelle dich der Rechten und versuche, ihre Pläne öffentlich zu entlarven.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            hide_and_plan()
            break
        elif choice == "2":
            expose_right()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def media_campaign():
    while True:
        print("\n--- Medienkampagne ---")
        print("Du schlägst vor, eine Medienkampagne zu starten, um die Öffentlichkeit zu mobilisieren. Die Gruppe stimmt zu, und ihr beginnt, eure Botschaft über soziale Netzwerke und unabhängige Medien zu verbreiten.")
        print("Die Kampagne wird viral, und immer mehr Menschen beginnen, sich der Bewegung anzuschließen.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Versuche, durch Crowdfunding Gelder für eure Aktionen zu sammeln.")
        print("2. Organisiere eine Online-Debatte mit einem prominenten Vertreter der Rechten.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            crowdfunding()
            break
        elif choice == "2":
            online_debate()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def negotiate_with_center():
    while True:
        print("\n--- Verhandlungen mit der Mitte ---")
        print("Du triffst dich mit Vertretern der Mitte, um sie davon zu überzeugen, eure Bewegung zu unterstützen. Sie sind vorsichtig, aber sie sehen die Notwendigkeit, gemeinsam gegen die Rechte vorzugehen.")
        print("Nach langen Diskussionen erklären sie sich bereit, eine gemeinsame Erklärung gegen die rechte Gewalt abzugeben.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Suche nach weiteren potenziellen Verbündeten, um die Allianz zu erweitern.")
        print("2. Organisiere eine groß angelegte Kampagne, um die Mitte stärker in die Bewegung einzubinden.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            recruit_allies()
            break
        elif choice == "2":
            middle_campaign()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def crowdfunding():
    while True:
        print("\n--- Crowdfunding ---")
        print("Du startest eine Crowdfunding-Kampagne, um Gelder für eure Aktionen zu sammeln. Die Kampagne ist ein Erfolg, und ihr habt nun die Mittel, um größere Aktionen zu planen.")
        print("Mit den neuen Ressourcen beginnt ihr, professioneller zu arbeiten und größere Aktionen zu organisieren.")
        print("\nWie möchtest du die Gelder verwenden?")
        print("1. Finanziere friedliche Demonstrationen und Aufklärungskampagnen.")
        print("2. Investiere in verdeckte Operationen, um die rechte Bewegung zu unterminieren.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            fund_peaceful_protests()
            break
        elif choice == "2":
            fund_covert_operations()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def recruit_allies():
    while True:
        print("\n--- Neue Verbündete ---")
        print("Du beginnst, weitere potenzielle Verbündete aus verschiedenen politischen und sozialen Gruppen zu rekrutieren. Dabei stößt du auf verschiedene Herausforderungen und Konflikte.")
        print("\nWie möchtest du vorgehen?")
        print("1. Versuche, zwischen den unterschiedlichen Gruppen zu vermitteln.")
        print("2. Konzentriere dich auf die stärksten Gruppen und lass die schwächeren beiseite.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            mediate_groups()
            break
        elif choice == "2":
            focus_on_strong_groups()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def middle_campaign():
    while True:
        print("\n--- Kampagne ---")
        print("Du organisierst eine groß angelegte Kampagne, um die Mitte stärker in die Bewegung einzubinden. Die Kampagne ist erfolgreich, und immer mehr Menschen schließen sich der Bewegung an.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Nutze die Dynamik, um eine nationale Bewegung zu starten.")
        print("2. Setze auf lokale Aktionen, um die Unterstützung weiter zu festigen.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            national_movement()
            break
        elif choice == "2":
            local_actions()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def fund_peaceful_protests():
    while True:
        print("\n--- Friedliche Proteste ---")
        print("Du entscheidest dich, die Gelder in friedliche Demonstrationen und Aufklärungskampagnen zu investieren. Dies stärkt das öffentliche Bild der Bewegung und zieht weitere Unterstützer an.")
        print("\nWie möchtest du weiter vorgehen?")
        print("1. Organisiere eine große Demonstration in der Hauptstadt, um den Erfolg zu zeigen.")
        print("2. Nutze die Mittel, um Bildungsprogramme zu fördern, die über die Gefahr der rechten Ideologie aufklären.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            larger_protest()
            break
        elif choice == "2":
            education_programs()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def fund_covert_operations():
    while True:
        print("\n--- Verdeckte Operationen ---")
        print("Du entscheidest dich, die Gelder in verdeckte Operationen zu investieren, um die rechte Bewegung zu unterminieren. Diese Strategie ist riskant, führt aber zu bedeutenden Erfolgen gegen die rechte Führung.")
        print("\nWie möchtest du die Operationen fortführen?")
        print("1. Fokussiere dich auf die Sabotage ihrer Kommunikationsmittel.")
        print("2. Setze auf Angriffe auf die finanziellen Unterstützer der rechten Bewegung.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            sabotage_communications()
            break
        elif choice == "2":
            attack_financial_backers()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def hide_and_plan():
    print("\n--- Verstecken und Planen ---")
    print("Du und deine Gruppe versteckt euch, um dem Zorn der Rechten zu entgehen. Während ihr euch versteckt, plant ihr eure nächsten Schritte sorgfältig.")
    print("Ihr entscheidet euch, die rechte Bewegung durch gezielte Aktionen zu schwächen.")
    print("\nWie möchtest du vorgehen?")
    print("1. Plane einen Angriff auf die Führung der rechten Bewegung.")
    print("2. Fokussiere dich auf die Verbreitung von Informationen, um die Rechte zu diskreditieren.")
    
    choice = input("> ").strip()
    
    if choice == "1":
        attack_leadership()
    elif choice == "2":
        information_campaign()
    else:
        print("Ungültige Eingabe, bitte versuche es erneut.")
        hide_and_plan()

def expose_right():
    print("\n--- Enthüllung ---")
    print("Du stellst dich der Rechten und versuchst, ihre Pläne öffentlich zu entlarven. Du organisierst eine Pressekonferenz und legst Beweise für ihre illegalen Aktivitäten vor.")
    print("Die Enthüllungen schlagen hohe Wellen, aber die Rechte schlägt hart zurück.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Setze die Enthüllungen fort und bringe weitere Informationen an die Öffentlichkeit.")
    print("2. Konzentriere dich darauf, die Bewegung zu schützen und das Risiko zu minimieren.")
    
    choice = input("> ").strip()
    
    if choice == "1":
        continue_exposure()
    elif choice == "2":
        risk_management()
    else:
        print("Ungültige Eingabe, bitte versuche es erneut.")
        expose_right()

def online_debate():
    while True:
        print("\n--- Online-Debatte ---")
        print("Du organisierst eine Online-Debatte mit einem prominenten Vertreter der Rechten. Die Debatte wird live gestreamt und zieht ein großes Publikum an.")
        print("Du bereitest dich gut vor und widerlegst seine Argumente souverän. Die Öffentlichkeit beginnt, die rechte Ideologie in Frage zu stellen.")
        print("\nWie möchtest du die Debatte nutzen?")
        print("1. Lade weitere prominente Vertreter ein, um die Diskussion zu erweitern.")
        print("2. Nutze die Debatte, um eine Petition zu starten und politische Maßnahmen zu fordern.")
        
        choice = input("> ").strip()
        
        if choice == "1":
            expand_debate()
            break
        elif choice == "2":
            start_petition()
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

def mediate_groups():
    print("\n--- Vermittlung ---")
    print("Du entscheidest dich, zwischen den unterschiedlichen Gruppen zu vermitteln, um eine breite Allianz zu schmieden. Nach harten Verhandlungen gelingt es dir, eine starke Koalition zu bilden.")
    print("\nWie möchtest du die Allianz nutzen?")
    print("1. Startet eine landesweite Kampagne, um den Widerstand zu verbreiten.")
    print("2. Nutzt die Allianz, um die rechte Bewegung direkt anzugreifen.")
    
    choice = input("> ").strip()
    
    if choice == "1":
        nationwide_campaign()
    elif choice == "2":
        direct_attack()
    else:
        print("Ungültige Eingabe, bitte versuche es erneut.")
        mediate_groups()

def focus_on_strong_groups():
    print("\n--- Fokussierung ---")
    print("Du konzentrierst dich auf die stärksten Gruppen, um eine effektive Widerstandsbewegung zu bilden. Dies führt jedoch zu Spannungen mit den schwächeren Gruppen, die sich ausgeschlossen fühlen.")
    print("\nWie möchtest du weitermachen?")
    print("1. Versuche, die Spannungen mit den schwächeren Gruppen zu lösen.")
    print("2. Ignoriere die Spannungen und setze auf eine starke, aber kleine Gruppe.")
    
    choice = input("> ").strip()
    
    if choice == "1":
        resolve_tensions()
    elif choice == "2":
        small_strong_group()
    else:
        print("Ungültige Eingabe, bitte versuche es erneut.")
        focus_on_strong_groups()

def larger_protest():
    print("\n--- Große Demonstration ---")
    print("Du organisierst eine große Demonstration in der Hauptstadt, um die Aufmerksamkeit auf eure Sache zu lenken. Die Demonstration zieht Tausende von Teilnehmern an und wird in den Medien stark beachtet.")
    print("\n--- Spiel Ende: Demonstration ---")
    print("Deine Entscheidung, die Bewegung in die Hauptstadt zu bringen, hat eure Botschaft verbreitet und die Unterstützung für den Widerstand gestärkt.")
    restart()

def education_programs():
    print("\n--- Bildungsprogramme ---")
    print("Du entscheidest dich, die Mittel zu nutzen, um Bildungsprogramme zu fördern, die über die Gefahren der rechten Ideologie aufklären. Diese Programme erreichen eine breite Zielgruppe und tragen dazu bei, die öffentliche Meinung zu verändern.")
    print("\n--- Spiel Ende: Aufklärung ---")
    print("Dank deiner Entscheidung, in Bildung zu investieren, wächst das Bewusstsein für die Probleme, die durch die rechte Ideologie verursacht werden.")
    restart()

def sabotage_communications():
    print("\n--- Kommunikationssabotage ---")
    print("Du entscheidest dich, die Kommunikationsmittel der rechten Bewegung zu sabotieren. Diese Aktion stört ihre Organisation erheblich und schwächt ihre Fähigkeit, schnell zu reagieren.")
    print("\n--- Spiel Ende: Sabotage Erfolg ---")
    print("Deine Entscheidung, ihre Kommunikationswege zu unterbrechen, hat die rechte Bewegung entscheidend geschwächt.")
    restart()

def attack_financial_backers():
    print("\n--- Angriff auf finanzielle Unterstützer ---")
    print("Du richtest deine Angriffe auf die finanziellen Unterstützer der rechten Bewegung. Diese Aktion destabilisiert ihre Finanzierung und zwingt sie, ihre Aktivitäten zu reduzieren.")
    print("\n--- Spiel Ende: Finanzielle Sabotage ---")
    print("Durch den Erfolg deiner Angriffe auf ihre Finanzen wurde die rechte Bewegung erheblich geschwächt.")
    restart()

def attack_leadership():
    print("\n--- Angriff auf die Führung ---")
    print("Du planst einen gezielten Angriff auf die Führung der rechten Bewegung. Dies schwächt ihre Organisation erheblich, aber es führt auch zu erhöhter Gewaltbereitschaft auf ihrer Seite.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Setze weitere Angriffe auf die Führung fort.")
    print("2. Ziehe dich zurück und beobachte die Reaktion der Rechten.")

def information_campaign():
    print("\n--- Informationskampagne ---")
    print("Du entscheidest dich, eine Informationskampagne zu starten, um die rechte Bewegung öffentlich zu diskreditieren. Dies führt dazu, dass ihre Anhängerschaft schrumpft und die Unterstützung in der Bevölkerung abnimmt.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Verbreite noch mehr Informationen, um die Bewegung weiter zu schwächen.")
    print("2. Konzentriere dich auf den Aufbau von Bündnissen, die eure Bewegung unterstützen.")

def continue_exposure():
    print("\n--- Fortsetzung der Enthüllungen ---")
    print("Du entscheidest dich, weitere Informationen über die rechte Bewegung öffentlich zu machen. Dies führt zu wachsendem Druck auf die rechte Führung, aber auch zu verstärkten Gegenmaßnahmen.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Veröffentliche alle gesammelten Informationen auf einmal.")
    print("2. Veröffentliche die Informationen schrittweise, um den Druck über einen längeren Zeitraum aufrechtzuerhalten.")

def risk_management():
    print("\n--- Risikomanagement ---")
    print("Du entscheidest dich, die Bewegung zu schützen und das Risiko zu minimieren. Dadurch handelst du vorsichtiger, aber es erlaubt dir, die Bewegung langfristig stabil zu halten.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Baue sichere Kommunikationskanäle auf, um die Bewegung zu koordinieren.")
    print("2. Entwickle Strategien, um die Sicherheit der Mitglieder zu gewährleisten.")

def expand_debate():
    print("\n--- Erweiterte Debatte ---")
    print("Du lädst weitere prominente Vertreter ein, um die Diskussion zu erweitern. Die Debatte erreicht ein noch größeres Publikum und gewinnt an Tiefe und Einfluss.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Organisiere eine Serie von Debatten, um die Öffentlichkeit weiter zu sensibilisieren.")
    print("2. Nutze die Debatte, um konkrete politische Forderungen zu stellen.")

def start_petition():
    print("\n--- Petition ---")
    print("Du nutzt die Debatte, um eine Petition zu starten und politische Maßnahmen zu fordern. Die Petition gewinnt schnell an Unterstützung und übt Druck auf die Regierung aus.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Verwende die Unterschriften, um einen direkten Dialog mit der Regierung zu erzwingen.")
    print("2. Organisiere eine Massenkundgebung, um die Unterstützung für die Petition zu demonstrieren.")

def direct_attack():
    print("\n--- Direkter Angriff ---")
    print("Du entscheidest dich, die rechte Bewegung direkt anzugreifen, indem du ihre wichtigsten Mitglieder und Infrastrukturen ins Visier nimmst. Dies führt zu massiven Unruhen und einer Eskalation des Konflikts.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Führe weitere Angriffe durch, um die Rechten zu destabilisieren.")
    print("2. Nutze die Unruhen, um eine breite Mobilisierung der Bevölkerung zu erreichen.")

def resolve_tensions():
    print("\n--- Spannungen lösen ---")
    print("Du arbeitest hart daran, die Spannungen zwischen den verschiedenen Gruppen in deiner Allianz zu lösen. Durch geschickte Verhandlungen und Kompromisse schaffst du es, die Einheit zu bewahren.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Führe regelmäßige Treffen durch, um den Zusammenhalt der Allianz zu stärken.")
    print("2. Entwickle gemeinsame Ziele und Strategien, um die Allianz zu festigen.")

def small_strong_group():
    print("\n--- Kleine, starke Gruppe ---")
    print("Du entscheidest dich, dich auf eine kleine, aber starke Gruppe zu konzentrieren. Diese Gruppe ist hocheffizient, aber die fehlende breite Unterstützung macht sie anfälliger für Gegenangriffe.")
    print("\nWie möchtest du weiter vorgehen?")
    print("1. Rekrutiere gezielt neue Mitglieder, um die Gruppe zu verstärken.")
    print("2. Entwickle spezialisierte Taktiken, um die Effektivität der kleinen Gruppe zu maximieren.")


def restart():
    while True:
        print("\nMöchtest du das Spiel erneut spielen? (ja/nein)")
        
        choice = input("> ").strip().lower()
        
        if choice == "ja":
            start_game()
            break
        elif choice == "nein":
            print("Danke fürs Spielen!")
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

# Spiel starten
start_game()
