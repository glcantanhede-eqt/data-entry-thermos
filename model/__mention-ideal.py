class Mention():
    def __init__(self, label, polarity, tags):
        self.label = label # A short description of the mention
        self.polarity = polarity # Positive, Neutral or Negative
        self.tags = tags # Which tags fit the mention. E.g. Power Outage, 
        self.observations = {
            "positive":None,
            "warn":None
        }

    #TODO Here we need to implement some string validation techniques, 
    # to avoid bad input or sql injection threats on freeform input
    def validate_observation(txt_observation):
        # do some regex magic, and some sql inject countermeasures 
        return None

    def insert_observations(self, pos_obs, warn_obs):
        self.observations["positive"] = pos_obs if pos_obs else None
        self.observations["warn"] = warn_obs if warn_obs else None
        

class Digital_Mention(Mention):
    def __init__(self, label, polatiry, tags, platform, reach):
        Mention.__init__(self, label, polatiry, tags)
        self.platform = platform #where we were mentioned. E.g. Instagram, Tiktok, Facebook
        self.reach = reach #how many likes, shares, comments etc. the mention got

class Press_Mention(Mention):
    def __init__(self, label, polatiry, tags, carrier, relevance, modality):
        Mention.__init__(self, label, polatiry, tags)
        self.carrier = carrier #E.g. Folha de São Paulo
        self.relevance = relevance #how impactful the carrier is. E.g. Globo News
        self.modality = modality #type of news. E.g. Newspaper, TV news channel, news blog


        