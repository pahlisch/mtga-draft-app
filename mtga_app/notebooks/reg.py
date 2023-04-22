try:
    set_df_kw['counterspell'] = np.where((set_df_kw['counter_tkn']==1) &

                                            ((set_df_kw['oracle_text'].str.lower().str.contains("counter target")) |
                                            (set_df_kw['oracle_text'].str.lower().str.contains("counter all")) |
                                            (set_df_kw['oracle_text'].str.lower().str.contains("counter it")))
                                            ,1,0)
except:
    set_df_kw['counterspell'] = 0

set_df_kw['manarock'] = np.where(
                                ((set_df_kw['tapping_ability']==1) |
                                    (set_df_kw['oracle_text']).str.lower().str.contains("tap")) &

                                (set_df_kw['type_line']).str.lower().str.contains("artifact") &

                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"{t}: add.*?(mana of any color|mana of that color|{(.*?)})",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"{t}, tap an untapped.*?(mana of any color|mana of that color|{(.*?)})",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"{t}: choose a color",regex=True)==True)
                                )
                                ,1,0)

set_df_kw['manadork'] = np.where(
                                (set_df_kw['tapping_ability']==1)&
                                (set_df_kw['manarock']!=1) &
                                (set_df_kw['back_type']!="Land") &
                                (set_df_kw['type_line']).str.lower().str.contains("creature") &

                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"{t}: add",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"{t}:.*?add one mana",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"{t}: add",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"add (one|two|three|four|five) mana",regex=True)==True)
                                )
                                ,1,0)


set_df_kw['removal'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(f"(destroy|exile) target ({regex_1}|({regex_1}, {regex_1})|({regex_1}, {regex_1}, {regex_1})|({regex_1}, {regex_1}, {regex_1}, {regex_1})) (creature|permanent)(?! from (a|your) graveyard| card from (a|your) graveyard)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(destroy|exile) another target (creature|permanent)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"destroy any number of target (creature|creatures|permanent|permanents)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(destroy|exile) target (attacking|blocking|attacking or blocking) creature",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"destroy up to (one|two|three) target (\w+) (creature|permanent|creatures|permanents)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"exile up to (one|two|three) target (creature|permanent|creatures|permanents)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"exile up to (one|two|three) target (nonland|nonartifact) (creature|permanent|creatures|permanents)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"exile up to (one|two|three) target (\w+) (\w+) (creature|permanent|creatures|permanents)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(destroy|exile) target (\w+) or creature",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(destroy|exile) a (creature|permanent) with the (greatest|highest|lowest) (power|toughness|converted mana cost|mana value)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(destroy|exile) target (creature|permanent)(?! from a graveyard| card from a graveyard)", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(destroy|exile) up to (\w+) target (attacking or blocking|attacking|blocking) (creature|creatures)", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"target (player|opponent) sacrifices a (creature|permanent)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"each (player|opponent) sacrifices (a|one|two|three|four) (creature|creatures|permanent|permanents)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted (creature|permanent) is a treasure",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted creature doesn't untap",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(annihilator)")==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"deals damage equal to its power to target creature",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(fights|fight) target creature")==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(those creatures|the chosen creatures) fight each other",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(fights|fight) up to (\w+) target (creature|creatures)", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(fights|fight) another target creature",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"choose target creature you don't control.*?each creature.*?deals damage equal.*?to that creature",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"you may have (cardname|it) fight (that creature|target creature|another target creature)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"target creature deals damage to itself equal to (its power)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"target creature gets -[0-9]/-[2-9]", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"target creature gets \+[0-9]/-[2-9]", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"target creature an opponent controls gets \-[0-9]/\-[2-9]", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted creature (gets|has).*?loses (all|all other) abilities", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted creature gets \-[0-9]/\-[2-9]", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted creature gets \-[0-9]/\-[2-9]", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted creature gets \+[0-9]/\-[2-9]", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(enchanted|target) creature gets \-[0-9][0-9]/\-[0-9][0-9]", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains("target creature gets \-x/\-x")==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains("target creature gets \+x/\-x")==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"target creature an opponent controls gets \-x/\-x", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted creature gets \-x/\-x", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted (creature|permanent) can't attack or block",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains("enchanted creature has defender")==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains("enchanted creature can't block.*?its activated abilities can't be activated")==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted creature.*?loses all abilities",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted (creature|permanent) can't attack.*?block.*?and its activated abilities can't be activated", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"deals ([2-9|x]) damage.*?(creature|any target|divided as you choose|to each of them)", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"deals ([2-9|x]) damage.*?to each of up to (one|two|three|four) (target|targets)", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"deals damage equal to.*?to (any target|target creature|target attacking creature|target blocking creature|target attacking or blocking creature)", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"target creature deals (.*?) damage to itself", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"deals damage to (any target|target creature|target attacking creature|target blocking creature|target attacking or blocking creature).*?equal to", regex=True)==True)) &

                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(cardname|it) deals [a-zA-Z0-9] damage to that player.",regex=True)==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains("(cardname|it) deals [a-zA-Z0-9] damage to target (player|opponent) or planeswalker")==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains("(cardname|it) deals [a-zA-Z0-9] damage to that creature's controller")==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains("that was dealt damage this turn")==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains("^(?!damage|creature)\w* random")==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"search.*?(creature|artifact|enchantment) card",regex=True)==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(destroy|exile) target land",regex=True)==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains("return it to the battlefield")==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"return that (card|creature|permanent) to the battlefield",regex=True)==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"if you control a.*?^(?!liliana)\w* planeswalker",regex=True)==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"^(?!additional cost|additional cost)\w* exile (target|a|one|two|three|all).*?from (your|a|target opponent's) graveyard",regex=True)==False)
                                    ,1,0)

set_df_kw['wrath'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(destroy|exile) (all|all other|each|each other|all attacking) (creature|creatures|(.*?) creatures|permanent|permanents|(.*?) permanents|(nonland|multicolored) permanent|(nonland|multicolored) permanents)",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"each (creature|other creature) gets -(x|[0-9])/-(x|[2-9])", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"each creature deals damage to itself equal to", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(destroy|exile) all artifacts, creatures, and enchantments", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"sacrifices (all|that many) (creatures|(.*?) creatures|permanents|(.*?) permanents)", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"chooses.*?then sacrifices the rest", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"creatures.*?get -(x|[0-9])/-(x|[2-9])", regex=True)==True) | #Crippling Fear
                                (set_df_kw['oracle_text'].str.lower().str.contains(f"deals ([3-9]|x|[1-9][0-9]) damage to each (creature|{regex_1} creature)", regex=True)==True)
                                )
                                ,1,0)

regex_2 = "(land|lands|basic land|basic lands|plains|island|swamp|mountain|forest|plains|islands|swamps|mountains|forests|basic plains|basic island|basic swamp|basic mountain|basic forest|basic plains|basic islands|basic swamps|basic mountains|basic forests)"

regex_3 = "(a|one|one|two|three|up to one|up to two|up to three|up to ten|up to x|x)"

set_df_kw['ramp'] = np.where(
                            (set_df_kw['face_type']!="Land") &
                            (set_df_kw['manadork']!=1) &
                            (set_df_kw['manarock']!=1) &
                            (set_df_kw['face_type']!="Snow Land") &
                            (set_df_kw['face_type']!="Artifact Land") &
                            (set_df_kw['type_line'].str.lower().str.contains(r"(\w+) // land", regex=True)==False) &
                            (
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"{t}: add", regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"^(?!{[1-9]}: )\w* add (one|two) mana", regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"{[1]}, {t}: add ({(c|w|u|b|r|g)}{(c|w|u|b|r|g)}|two)", regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"whenever enchanted land is tapped for mana.*?adds", regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(f"search (your|their) library for {regex_3} {regex_2}.*?put.*?onto the battlefield", regex=True)==True)
                            ) &
                            (
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"{[1-9]}, {t}: add one mana", regex=True)==False) &
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted land.*?{t}: add {(c|1|w|u|b|r|g)}", regex=True)==False) &
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"destroy target (land|nonbasic land)", regex=True)==False) &
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"spend this mana only to", regex=True)==False)
                            )
                            ,1,0)

set_df_kw['tutor'] = np.where(
                            (set_df_kw['ramp']!=1) &
                            (set_df_kw['face_type']!="Land") &
                            (set_df_kw['face_type']!="Snow Land") &
                            (set_df_kw['face_type']!="Artifact Land") &
                            (
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"search your (library|library and graveyard) for (a|an|any|any one|one|up to one|two|up to two|three|up to three|four|up to four|a(white|blue|black|red|green|colorless)) (card|cards|permanent|permanents|equipment|aura|aura or equipment|legendary|enchantment|enchantments|artifact|artifacts|creature|(.*?) creature cards|creature cards|creatures|sorcery|sorceries|instant|instants|planeswalker)", regex=True)==True)
                            ) &
                            (
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"put (it|them|those cards|that card) into your graveyard", regex=True)==False) &
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"named", regex=True)==False)
                            )
                            ,1,0)

set_df_kw['cardraw'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"draw (a|one|two|three|four|five|six|seven|x|(.*?) x) (card|cards)", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"draw (cards equal to|that many cards)", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"target player draws (.*?) (card|cards)", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(look at|reveal) the.*?put.*?(into|in) your hand", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(exile|look at the).*?(card|cards).*?you may (cast|play)", regex=True)==True)
                                ) &
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"whenever you draw a card", regex=True)==False) &
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"if you would draw a card", regex=True)==False) &
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"draw (a|one|two|three|four) (card|cards), then discard (a|one|two|three|four) (card|cards)", regex=True)==False) &
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"discard (a|one|two|three|four) (card|cards), then draw (a|one|two|three|four) (card|cards)", regex=True)==False)
                                )
                                ,1,0)

set_df_kw['burn'] = np.where(
                            (
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"deals ([1-9|x]) damage.*?(any target|player|opponent|to them|to each of them)", regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"deals (x|two|three|four|five) times (damage|x damage).*?(any target|player|opponent|to them|to each of up to)", regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"deals damage equal to.*?to (any target|target player|target opponent|to them|each player|each opponent)", regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"deals damage to (any target|target player|target opponent|to them|each player|each opponent).*?equal to", regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"deals that much damage to (any target|target player|target opponent|each player|each opponent|that source's controller)", regex=True)==True)
                            )
                            ,1,0)

set_df_kw['discard'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(that|target|each) (player|opponent) discards (a|one|two|three|that|all|all the) (card|cards)", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"unless that player.*?discards a card", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"target (player|opponent) reveals their hand.*?you choose.*?exile (that|it)", regex=True)==True)
                                )
                                ,1,0)

set_df_kw['enters_bf'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(enter|enters) the battlefield", regex=True)==True)
                                )
                                &
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(enter|enters) the battlefield tapped", regex=True)==False) &
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"land (enter|enters) the battlefield", regex=True)==False) &
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"it becomes day", regex=True)==False) &
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"enchant creature", regex=True)==False)
                                )
                                ,1,0)

set_df_kw['die_trigger'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"when (cardname|equipped creature) dies", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"whenever.*?dies", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"whenever.*?you (control|don't control) dies", regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['attack_trigger'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(when|whenever) (cardname|equipped creature|it) attacks", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(when|whenever) (cardname|equipped creature|it) and.*?(other|another) (creature|creatures) attack", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(battalion|exert|raid)", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(when|whenever) (cardname|equipped creature|it) enters the battlefield or attacks", regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['pseudo_ramp'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"you may put a (land|basic land).*?onto the battlefield", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(you|each player) may (play|put) an additional land", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"if it's a land card, you may put it onto the battlefield", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"sacrifice.*?add.*?({(.*?)}|to your mana pool|mana of (any|any one) color)", regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['static_ramp'] = np.where(
                                    ((set_df_kw['type_line'].str.lower().str.contains("enchantment")) |
                                    (set_df_kw['type_line'].str.lower().str.contains("creature")) |
                                    (set_df_kw['type_line'].str.lower().str.contains("artifact"))) &
                                    (set_df_kw['back'].str.lower().str.contains("land")==False) &
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"at the beginning of.*?add.*?(mana|{(.*?)})", regex=True)==True)
                                    )
                                    ,1,0)

regex_4 = "(a|one|up to one|two|up to two|three|up to three|four|up to four|five|up to five|six|up to six|x|up to x)"

set_df_kw['creature_tokens'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(f"(create|put) {regex_4}.*?creature (token|tokens)", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(f"(living weapon|amass|fabricate|afterlife|populate)", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(creature tokens|creature tokens with.*?) are created instead", regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['extra_turn'] = np.where(set_df_kw['oracle_text'].str.lower().str.contains(r"(take|takes) (an|one|two) extra (turn|turns)", regex=True)==True
                                    ,1,0)

set_df_kw['plus1_counters'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"\+1/\+1 (counter|counters)", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(evolve|mentor|adapt|bolster|bloodthirst|devour|monstrosity|reinforce|training)", regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['graveyard_hate'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"exile.*?from (graveyards|a graveyard|his or her graveyard|target player's graveyard|each opponent's graveyard)", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"remove all graveyards from the game", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"exile.*?all (cards|creatures) from all (graveyards|opponents' hands and graveyards)", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"exile each opponent's graveyard", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"if a.*?(card|creature|permanent) would (be put into.*?graveyard|die).*?(instead exile|exile it instead)", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"choose target card in (target opponent's|a) graveyard.*?exile (it|them)", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(target|each) player puts all the cards from their graveyard", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(creature cards|permanents|creatures|permanent cards) in (graveyards|graveyards and libraries) can't enter the battlefield", regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['free_spells'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(rather than pay|without paying) (its|it's|their|this spell's|the) mana cost", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"cascade", regex=True)==True)
                                    )
                                    &
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"you may pay {", regex=True)==False)
                                    )
                                    ,1,0)

set_df_kw['bounce_spell'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"return.*?to (it's|its|their) (owner's|owners') (hand|hands)", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"owner.*?puts it.*?(top|bottom).*?library", regex=True)==True)
                                    )
                                    &
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"^(?!islands)\w* you control", regex=True)==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(when|whenever).*?dies.*?return.*?to its owner's hand", regex=True)==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"return (cardname|the exiled card) to its owner's hand", regex=True)==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"whenever cardname.*?return it to its owner's hand", regex=True)==False)
                                    )
                                    ,1,0)

set_df_kw['sac_outlet'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"sacrifice (a|another) (creature|permanent)", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(exploit)", regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['sac_payoff'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"whenever (you|a player) (sacrifice|sacrifices) a (creature|permanent)", regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['cant_counter'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"can't be countered", regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['costx_more'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(cost|costs) (.*?) more to cast", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"ward", regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['costx_moreactivate'] = np.where(
                                            (
                                            (set_df_kw['oracle_text'].str.lower().str.contains(r"(cost|costs) (.*?) more to activate", regex=True)==True)
                                            )
                                            ,1,0)

set_df_kw['costx_less'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(cost|costs) (.*?) less to cast", regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['costx_lessacitivate'] = np.where(
                                            (
                                            (set_df_kw['oracle_text'].str.lower().str.contains(r"(cost|costs) (.*?) less to activate", regex=True)==True)
                                            )
                                            ,1,0)

set_df_kw['whenever_opp'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"whenever (an opponent|a player)", regex=True)==True)
                                    )
                                    ,1,0)

regex_5 = "(all|each|another|another target|x|x target|a|target|any number of|one|up to one|up to one target|two|up to two|up to two target|three|up to three|up to three target|four|up to four|up to four target)"
regex_6 = "(card|cards|creature|creatures|nonlegendary creature|creature card|creature cards|permanent|permanents|permanent card|permanent cards|land|lands|land card|land cards|instant or sorcery card|equipment card|aura card|aura or equipment card|artifact or enchantment)"

set_df_kw['returnfrom_gy'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(fr"return {regex_5} {regex_6}.*?from your graveyard to your hand", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(fr"return cardname from your graveyard to your hand", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(fr"choose.*?graveyard.*?return.*?to your hand", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(fr"return.*?up to.*?from your graveyard to your hand", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(fr"return (target|another target).*?card from your graveyard to your hand", regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['reanimation'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(fr"(return|put) {regex_5} {regex_6}.*?from (your|a) graveyard (to|onto) the battlefield", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(fr"return cardname from your graveyard to the battlefield", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(fr"choose.*?graveyard.*?return.*?to the battlefield", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(fr"return.*?up to.*?from your graveyard to the battlefield", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(fr"enchant creature card in (a|your) graveyard.*?return enchanted creature card to the battlefield under your control", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(fr"(return|returns|put) (all|any number of) (creature|permanent|enchantment|artifact|legendary permanent|legendary creature|nonlegendary creature|nonlegendary permanents|(.*?), (.*?) and (.*?)) cards.*?from (their|your|all) (graveyard|graveyards) (to|onto) the battlefield", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(fr"(return|put) (target|another target).*?card from your graveyard to the battlefield", regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['castfrom_gy'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"you may cast cardname from your graveyard", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"flashback {", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"jump-start", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"escape—{", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"disturb {", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"unearth {", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"retrace", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"embalm", regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['lord'] = np.where(
                            (
                            (set_df_kw['type_line'].str.lower().str.contains("creature")) |
                            (set_df_kw['type_line'].str.lower().str.contains("artifact")) |
                            (set_df_kw['type_line'].str.lower().str.contains("enchantment"))
                            ) &
                            (
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"get \+[1-9]/\+[0-9]", regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"(battle cry)", regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"each (creature|other creature).*?gets \+[1-9]/\+[0-9]", regex=True)==True)
                            )
                            &
                            (
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"until end of turn", regex=True)==False)
                            )
                            ,1,0)

set_df_kw['upkeep_trigger'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"beginning of (your|enchanted player's|each|each player's) upkeep", regex=True)==True)
                                        )
                                        &
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"beginning of your upkeep, sacrifice cardname", regex=True)==False)
                                        )
                                        ,1,0)

set_df_kw['endstep_trigger'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"beginning of (your|enchanted player's|each) end step", regex=True)==True)
                                        )
                                        &
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"sacrifice.*? at the beginning of your end step", regex=True)==False)
                                        )
                                        ,1,0)

set_df_kw['landfall'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"whenever a land enters the battlefield under your control", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"landfall", regex=True)==True)
                                )
                                ,1,0)

set_df_kw['combat_trigger'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"beginning of (combat|each combat)", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"deals combat damage", regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['life_gain'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"gain (.*?) life", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"gains (.*?) x life", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"gain life equal", regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(lifelink|extort)", regex=True)==True)
                                )
                                ,1,0)

set_df_kw['treasure_tokens'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(f"(create|put) {regex_4}.*?treasure (token|tokens)", regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['protection'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(f"(hexproof|ward|indestructible|shroud)", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(f"can't (be|become) (the|target)", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(f"protection from", regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(f"becomes the target of a spell", regex=True)==True)
                                    )
                                    &
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"becomes the target of.*?sacrifice (it|cardname)", regex=True)==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"becomes the target of.*?shuffle.*?into its owner's library", regex=True)==False) &
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"becomes.*?with hexproof.*?until end of turn", regex=True)==False)
                                    )
                                    ,1,0)

set_df_kw['cost_reduction'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(delve|convoke|affinity|foretell|madness|miracle|spectacle)", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"evoke", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"you may pay.*?to cast this spell", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"you may pay (.*?) rather than pay", regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['mana_multipliers'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(whenever|if).*?tap (a|an) (land|permanent|nonland permanent|plains|island|swamp|mountain|forest|creature) for mana.*?add (one mana|an additional|{(.*?)})", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(whenever|if).*?tap (a|an) (land|permanent|nonland permanent|plains|island|swamp|mountain|forest|creature) for mana.*?it produces.*?instead", regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['card_selection'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"scry", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"look at the top.*?bottom of your library.*?on top", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"look at the top.*?on top.*?bottom of your library", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"look at the top.*?graveyard.*?on top", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"look at the top.*?on top.*?graveyard", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"look at the top.*?you may put.*?into your graveyard", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"surveil", regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(explore|explores)", regex=True)==True)
                                        )
                                        &
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"whenever a creature you control explores", regex=True)==False)
                                        )
                                        ,1,0)

set_df_kw['whenever_cast'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(whenever you cast|prowess)",regex=True)==True)
                                        )
                                        &
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"you may transform", regex=True)==False)
                                        )
                                        ,1,0)

set_df_kw['gain_control'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"gain control of",regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['unblockeable'] = np.where(
                                    (set_df_kw['type_line'].str.lower().str.contains("creature")) &
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(cardname|you control) can't be blocked",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(unblockable|shadow)",regex=True)==True)
                                    )
                                    &
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"cardname can't be blocked by", regex=True)==False)
                                    )
                                    ,1,0)

set_df_kw['difficult_block'] = np.where(
                                        (set_df_kw['type_line'].str.lower().str.contains("creature")) &
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"cardname can't be blocked by",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(menace|first strike|flying|deathtouch|double strike|fear|intimidate)",regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['create_copy'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"create a copy of",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(that's|as) a copy of",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"copy (target|it|them|that spell|that ability)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"you may copy",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(storm)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"becomes a copy",regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['milling'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(mill|mills)",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"puts the top.*?of (their|his or her|your) library into (their|his or her|your) graveyard",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"exile the top (.*?) cards of (target|each) (player|opponent|players|opponents)",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(target|each) opponent exiles cards from the top of their library",regex=True)==True)
                                )
                                ,1,0)

set_df_kw['trigger_multiplier'] = np.where(
                                            (
                                            (set_df_kw['oracle_text'].str.lower().str.contains(r"triggers (one more|an additional) time",regex=True)==True)
                                            )
                                            ,1,0)

set_df_kw['untapper'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"untap (target|that|another|the chosen|them|all)",regex=True)==True)
                                )
                                &
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"gain control", regex=True)==False)
                                )
                                ,1,0)

set_df_kw['static_effects'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(artifacts and creatures|creatures|permanents) (your opponents|enchanted player|you) (control|controls) (enter|lose|have|with|can't)",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"activated abilities of (artifacts|creatures).*?can't be activated",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"can't cause their controller to search their library",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"don't cause abilities to trigger",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"can't draw more than",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"only any time they could cast a sorcery",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"enchanted player",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"at the beginning of (your|each).*?(you|that player)",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(players|counters) can't",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"if (you|target opponent|a player|another player) would.*?instead",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"each (card|(.*?) card) in your (hand|graveyard).*?has",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"(each player|players|your opponents) can't cast (spells|more than)",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"is determined by their (power|toughness) rather than their (power|toughness)",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"each creature.*?assigns combat damage.*?toughness rather than its power",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"they put half that many",regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['damage_multipliers'] = np.where(
                                            (
                                            (set_df_kw['oracle_text'].str.lower().str.contains(r"it deals that much damage plus",regex=True)==True) |
                                            (set_df_kw['oracle_text'].str.lower().str.contains(r"it deals (double|triple) that damage",regex=True)==True)
                                            )
                                            ,1,0)


set_df_kw['agressive'] = np.where(
                                    (set_df_kw['type_line'].str.lower().str.contains("creature")) &
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(haste|riot|dash)",regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['doublers'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(put|it creates|it puts|create) twice that many",regex=True)==True)
                                )
                                ,1,0)

set_df_kw['blinker'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"exile (up to (one|two) target|up to (one|two) other target|target|another target|any number of target) (creature|creatures|(.*?) creature|permanent|permanents|(.*?) permanent|(.*?) or creature).*?return.*?to the battlefield",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"exile (target|another target) (permanent|creature).*?return (that card|that permanent|it) to the battlefield under its owner's control",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"exile (two|three|four|five|all|each).*?you (control|own).*?then return (them|those).*?to the battlefield",regex=True)==True)
                                )
                                ,1,0)

set_df_kw['graveyard_tutor'] = np.where(
                                        (set_df_kw['ramp']!=1) &
                                        (set_df_kw['tutor']!=1) &
                                        (set_df_kw['face_type']!="Land") &
                                        (set_df_kw['face_type']!="Snow Land") &
                                        (set_df_kw['face_type']!="Artifact Land") &
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"search your library for.*?put.*?into your graveyard", regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['play_toplibrary'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"play with the top of your library",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"you may (play|cast).*?(from the|the) top of your library",regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['life_lose'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(each opponent|each player|target opponent|target player).*?loses (.*?) life",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(afflict|extort)",regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['play_from_graveyard'] = np.where(
                                            (
                                            (set_df_kw['oracle_text'].str.lower().str.contains(r"you may (play|cast).*?(land|permanent|creature|artifact).*?from your graveyard",regex=True)==True)
                                            )
                                            ,1,0)

set_df_kw['infect'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"infect",regex=True)==True)
                                )
                                ,1,0)

set_df_kw['disenchant'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(destroy|exile) (target|each|every) (artifact or enchantment|artifact|enchantment)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"destroy (x) target (artifacts or enchantments|artifacts|enchantments)",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"destroy all (artifacts or enchantments|artifacts|enchantments)",regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['venture'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"venture into the dungeon",regex=True)==True)
                                )
                                ,1,0)

set_df_kw['animator'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"(target|another target).*?becomes a.*?creature",regex=True)==True)
                                )
                                &
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"copy", regex=True)==False) &
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"class", regex=True)==False))
                                ,1,0)

set_df_kw['wish'] = np.where(
                            (
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"you may.*?from outside the game",regex=True)==True) |
                            (set_df_kw['oracle_text'].str.lower().str.contains(r"learn",regex=True)==True)
                            )
                            ,1,0)

set_df_kw['gy_synergies'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"gets.*?for each.*?in your graveyard",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"(dredge)",regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['looting_similar'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"draw (a|one|two|three|four) (card|cards), then discard (a|one|two|three|four) (card|cards)",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"discard (a|one|two|three|four) (card|cards)(,|:) (draw|then draw) (a|one|two|three|four) (card|cards)",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"create (.*?) (blood|clue) token",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"cycling",regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['cheatinto_play'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"creature.*?put (it|them) onto the battlefield",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"look at the.*?put.*?creature.*?onto the battlefield",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"you may put.*?(creature|permanent).*?onto the battlefield",regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['pumped_foreach'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"gets \+[0-9]/\+[0-9] for each",regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['ritual'] = np.where(
                                (
                                (set_df_kw['type_line'].str.lower().str.contains("instant")) |
                                (set_df_kw['type_line'].str.lower().str.contains("sorcery"))
                                ) &
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"add {(.*?)}",regex=True)==True) |
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"add (.*?) {(.*?)}",regex=True)==True)
                                )
                                ,1,0)

set_df_kw['no_maximum'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"you have no maximum hand size",regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['wheel'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"each player.*?(discards|shuffles (his or her|their) hand and graveyard into (his or her|their) library).*?then draws seven cards",regex=True)==True)
                                )
                                ,1,0)

set_df_kw['extra_combat'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"additional combat phase",regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['ghostly_prison'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"creatures can't attack (you|you or planeswalkers you control) unless",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"whenever an opponent attacks (you|with creatures)",regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['land_destruction'] = np.where(
                                        (
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"destroy target (land|nonbasic land)",regex=True)==True) |
                                        (set_df_kw['oracle_text'].str.lower().str.contains(r"destroy all lands",regex=True)==True)
                                        )
                                        ,1,0)

set_df_kw['win_game'] = np.where(
                                (
                                (set_df_kw['oracle_text'].str.lower().str.contains(r"you win the game",regex=True)==True)
                                )
                                ,1,0)

set_df_kw['lose_game'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"you lose the game",regex=True)==True)
                                    )
                                    ,1,0)

set_df_kw['cant_lose'] = np.where(
                                    (
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"you can't lose the game",regex=True)==True) |
                                    (set_df_kw['oracle_text'].str.lower().str.contains(r"your opponents can't win the game",regex=True)==True)
                                    ) ,1,0)