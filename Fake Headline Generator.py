import random

politics_subjects = [
    "The Prime Minister",
    "Nirmala Sitharaman",
    "Rahul Gandhi",
    "Supreme Court of India",
    "Election Commission",
    "Indian Parliament",
    "A State Chief Minister",
    "A Lok Sabha MP",
    "A Political Strategist",
    "A Government Spokesperson"
]

entertainment_subjects = [
    "Shah Rukh Khan",
    "Salman Khan",
    "A Bollywood Director",
    "A Netflix India Show",
    "An Influencer Couple",
    "A Reality Show Contestant",
    "A South Indian Superstar",
    "A Film Critic",
    "A Paparazzi Photographer",
    "A Music Composer"
]

sports_subjects = [
    "Virat Kohli",
    "Rohit Sharma",
    "MS Dhoni",
    "Indian Cricket Team",
    "An IPL Franchise",
    "A Star Badminton Player",
    "Indian Olympic Contingent",
    "A Football Club Owner",
    "A Team Coach",
    "A Match Referee"
]

general_subjects = [
    "Indian Railways",
    "A Bangalore Startup",
    "A Mumbai Auto Driver",
    "An IIT Student",
    "A Group of Monkeys",
    "A Street Food Vendor",
    "A Tech Blogger",
    "An Overenthusiastic Uncle",
    "A Housing Society Secretary",
    "A WhatsApp Forward"
]

politics_actions = [
    "announces",
    "passes",
    "rejects",
    "addresses",
    "criticizes",
    "approves",
    "bans",
    "questions",
    "reviews",
    "debates"
]

politics_action_score = {
    "announces": 80,
    "passes": 85,
    "rejects": 70,
    "addresses": 78,
    "criticizes": 65,
    "approves": 82,
    "bans": 75,
    "questions": 68,
    "reviews": 72,
    "debates": 70
}


politics_places = [
    "inside Parliament",
    "at Red Fort",
    "during a press conference",
    "at India Gate",
    "inside Supreme Court",
    "during cabinet meeting",
    "at Raj Bhavan",
    "during election rally",
    "inside North Block",
    "on national television"
]

entertainment_actions = [
    "launches",
    "promotes",
    "reveals",
    "goes viral for",
    "announces",
    "gets trolled for",
    "collaborates with",
    "posts about",
    "reacts to",
    "walks out of"
]

entertainment_action_score = {
    "launches": 70,
    "promotes": 65,
    "reveals": 60,
    "goes viral for": 55,
    "announces": 68,
    "gets trolled for": 45,
    "collaborates with": 62,
    "posts about": 50,
    "reacts to": 52,
    "walks out of": 40
}

entertainment_places = [
    "at a movie premiere",
    "on Instagram Live",
    "during a press event",
    "at an award show",
    "inside a film studio",
    "on a reality show set",
    "during an interview",
    "at Mumbai airport",
    "on social media",
    "during film promotions"
]

sports_actions = [
    "wins",
    "loses",
    "breaks record at",
    "announces retirement at",
    "gets injured during",
    "celebrates victory at",
    "faces criticism after",
    "gets selected for",
    "gets dropped from",
    "appeals decision during"
]

sports_action_score = {
    "wins": 85,
    "loses": 65,
    "breaks record at": 90,
    "announces retirement at": 75,
    "gets injured during": 60,
    "celebrates victory at": 80,
    "faces criticism after": 55,
    "gets selected for": 78,
    "gets dropped from": 58,
    "appeals decision during": 62
}

sports_places = [
    "during an IPL match",
    "at Wankhede Stadium",
    "during a practice session",
    "at an international tournament",
    "inside the dressing room",
    "during the final match",
    "at a press conference",
    "on the field",
    "during medal ceremony",
    "at national camp"
]

general_actions = [
    "complains about",
    "celebrates",
    "gets stuck in",
    "accidentally invents",
    "goes viral for",
    "starts argument over",
    "discovers",
    "announces",
    "questions",
    "panics over"
]

general_action_score = {
    "complains about": 55,
    "celebrates": 50,
    "gets stuck in": 60,
    "accidentally invents": 45,
    "goes viral for": 52,
    "starts argument over": 40,
    "discovers": 58,
    "announces": 62,
    "questions": 48,
    "panics over": 35
}

general_places = [
    "in a Mumbai local train",
    "at a roadside tea stall",
    "inside an office meeting",
    "in Bengaluru traffic",
    "during a family function",
    "on WhatsApp group",
    "at a housing society",
    "on social media",
    "at a railway station",
    "during lunch break"
]

politics_subject_score = {
    "The Prime Minister": 85,
    "Nirmala Sitharaman": 80,
    "Rahul Gandhi": 78,
    "Supreme Court of India": 90,
    "Election Commission": 88,
    "Indian Parliament": 82,
    "A State Chief Minister": 75,
    "A Lok Sabha MP": 70,
    "A Political Strategist": 65,
    "A Government Spokesperson": 60
}

entertainment_subject_score = {
    "Shah Rukh Khan": 75,
    "Salman Khan": 73,
    "A Bollywood Director": 65,
    "A Netflix India Show": 60,
    "An Influencer Couple": 55,
    "A Reality Show Contestant": 50,
    "A South Indian Superstar": 70,
    "A Film Critic": 45,
    "A Paparazzi Photographer": 40,
    "A Music Composer": 58
}

sports_subject_score = {
    "Virat Kohli": 80,
    "Rohit Sharma": 78,
    "MS Dhoni": 85,
    "Indian Cricket Team": 82,
    "An IPL Franchise": 70,
    "A Star Badminton Player": 68,
    "Indian Olympic Contingent": 75,
    "A Football Club Owner": 60,
    "A Team Coach": 65,
    "A Match Referee": 55
}

general_subject_score = {
    "Indian Railways": 75,
    "A Bangalore Startup": 65,
    "A Mumbai Auto Driver": 55,
    "An IIT Student": 60,
    "A Group of Monkeys": 40,
    "A Street Food Vendor": 50,
    "A Tech Blogger": 45,
    "An Overenthusiastic Uncle": 35,
    "A Housing Society Secretary": 48,
    "A WhatsApp Forward": 30
}


flag = True


while flag:
    category=int(input("\n1)Politics\n2)Entertainment\n3)Sports\n4)General\nEnter Category:"))
    if (category==1):
        subject = random.choice(politics_subjects)
        action = random.choice(politics_actions)
        place_or_thing = random.choice(politics_places)

        headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"

        s_score = politics_subject_score.get(subject, 50)
        a_score = politics_action_score.get(action, 50)

        credibility = (s_score + a_score) // 2

        print("\n" + headline)
        print(f"Credibility Meter: {credibility}%")

        with open("Politics.txt", "a") as f:
            f.write(f"{headline} | Credibility: {credibility}%\n")

        user_input = input("\nEnter 'No' to stop generating new headlines: ")

        if user_input.lower() == "no":
            flag = False

    elif(category==2):
        subject = random.choice(entertainment_subjects)
        action = random.choice(entertainment_actions)
        place_or_thing = random.choice(entertainment_places)

        headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"

        s_score = entertainment_subject_score.get(subject, 50)
        a_score = entertainment_action_score.get(action, 50)

        credibility = (s_score + a_score) // 2

        print("\n" + headline)
        print(f"Credibility Meter: {credibility}%")

        with open("Entertainment.txt", "a") as f:
            f.write(f"{headline} | Credibility: {credibility}%\n")

        user_input = input("\nEnter 'No' to stop generating new headlines: ")

        if user_input.lower() == "no":
            flag = False

    elif(category==3):
        subject = random.choice(sports_subjects)
        action = random.choice(sports_actions)
        place_or_thing = random.choice(sports_places)

        headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"

        s_score = sports_subject_score.get(subject, 50)
        a_score = sports_action_score.get(action, 50)

        credibility = (s_score + a_score) // 2

        print("\n" + headline)
        print(f"Credibility Meter: {credibility}%")

        with open("Sports.txt", "a") as f:
            f.write(f"{headline} | Credibility: {credibility}%\n")

        user_input = input("\nEnter 'No' to stop generating new headlines: ")

        if user_input.lower() == "no":
            flag = False

    elif(category==4):
        subject = random.choice(general_subjects)
        action = random.choice(general_actions)
        place_or_thing = random.choice(general_places)

        headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"

        s_score = general_subject_score.get(subject, 50)
        a_score = general_action_score.get(action, 50)

        credibility = (s_score + a_score) // 2

        print("\n" + headline)
        print(f"Credibility Meter: {credibility}%")

        with open("General.txt", "a") as f:
            f.write(f"{headline} | Credibility: {credibility}%\n")

        user_input = input("\nEnter 'No' to stop generating new headlines: ")

        if user_input.lower() == "no":
            flag = False

    else:
        print("\n---Enter Correct Number---")
        flag = True
