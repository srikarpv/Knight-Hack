#{
#  "url": "https://gateway-a.watsonplatform.net/calls",
#  "note": "It may take up to 5 minutes for this key to become active",
#  "apikey": "d1d1b4981f8cda66770d4cf08199fdb8f0f2a0f3"
#}
import sys
import json
from watson_developer_cloud import AlchemyLanguageV1

def analyze_text(s):
    alchemy_language = AlchemyLanguageV1(api_key="d1d1b4981f8cda66770d4cf08199fdb8f0f2a0f3")
    response = alchemy_language.combined(
        url = s,
        extract = 'doc-emotion,doc-sentiment'
    )
    return response

def aggregate_speech_and_video(speech, video):
    #speech_json: anger, disgust, fear, joy, sadness
    #video_json: anger, disgust, fear, joy, surprise, neutral, sadness

    aggregate_video = {
    "anger": 0,
    "disgust": 0,
    "fear": 0,
    "joy": 0,
    "sadness": 0,
    "contempt": 0,
    "surprise": 0,
    "neutral": 0
    }

    for key in video:
        for value in video[key]:
            aggregate_video[key] += value

    for key in aggregate_video
        aggregate_video[key] = aggregate_video[key]/video["anger"].length

    result = {
    "anger": speech[anger] * (1/2) + aggregate_video[anger] * (1/2),
    "disgust": speech[disgust] * (1/2) + aggregate_video[disgust] * (1/2),
    "fear": speech[fear] * (1/2) + aggregate_video[fear] * (1/2),
    "joy": speech[joy] * (1/2) + aggregate_video[joy] * (1/2),
    "sadness": speech[sadness] * (1/2) + aggregate_video[sadness] * (1/2),
    "contempt": aggregate_video[contempt],
    "surprise": aggregate_video[surprise],
    "neutral": aggregate_video[neutral]
    }

    maximum = ""
    secondmax = ""
    for key, value in result:
        if value > maximum:
            maximum = key
        elif value > secondmax
            secondmax = key
    s = ""
    if maximum = "anger":
        if secondmax = "disgust":
            s = "Your primary emotions in speech and emotion are anger and disgust. Both have potentially destructive consequences; a possible explanation is entitlement and frustration to prevent change in function. Untense your body, breathe slowly, and smile."
        elif secondmax = "fear":
            s = "Your primary emotions are anger and fear. A possible explanation is initimidation and rationalization to meet one's own needs. Speakers perceived to be angry as a protective response, as in the case of fear, is a positive outlook, however, the stimuli inducing such fear may be irrationally perceived."
        elif secondmax = "joy":
            s = "We detect anger and joy as your primary emotions. The joy is a positive, energetic component of communication, and it is a possiblity that the anger component represents overeagerness and encroachment. We suggest you to embrace a more passive approach."
        elif secondmax = "sadness":
            s = "Anger and sadness are your primary signals. This combination suggests passive anger, which may result in evasivenss or subtle defeatism. This requires a more open approach to communication. If you haven’t already, open your palms and relax your shoulders."
        elif secondmax = "surprise":
            s = "Anger and surprise are your primary emotions. They suggest an intensity to your speaking and nonverbal communication with sudden changes and hostility. Smooth your speaking cadence and facial expressions."
        elif secondmax = "neutral":
            s = "Anger and neutral are your primary emotions. Neutral suggests passitivity while the pairing with anger suggests slight exaggerative response to some provocation."
        elif secondmax = "contempt":
            s = "Your primary emotions are anger and contempt. Assertive speaking should be for stability, not dominance. This hostile appearance may stem from an over-protective instinct."
    elif maximum = "disgust":
        if secondmax = "anger":
            s = "Your primary emotions in speech and emotion are anger and disgust. Both have potentially destructive consequences; a possible explanation is entitlement and frustration to prevent change in function. Untense your body, breathe slowly, and smile."
        elif secondmax = "fear":
            s = "Disgust and fear are your primary emotions. This suggests an indeterminably phobic body language and speech. "
        elif secondmax = "joy":
            s = "Disgust and joy are your primary emotions. This is somewhat conflicting stimulus and may represent fascination. Plutchik's theory of emotion describes this as positive communication."
        elif secondmax = "sadness":
            s = "Disgust and sadness are your primary emotions. While disgust implies a self-defensive reaction, sadness implies a more internal consequence. Most likely, disgust is detected from facial expressions."
        elif secondmax = "surprise":
            s = "Disgust and surprise are your primary emotions. If you are exaggerating facial expression, such as eyebrow-raising and mouth contortion, it may seem offputting to your audience."
        elif secondmax = "neutral":
            s = "Disgust and neutral are your primary emotions. Disgust is an aftereffect of social conditioning and is the easiest to detect. There may be a slight exaggeration in your facial expressions."
        elif secondmax = "contempt":
            s = "Disgust and contempt are your primary emotions. This might be a slight reactive mechanism towards some unpleasant stimuli. Disgust and contempt are the most recognizable facial behaviors."
    elif maximum = "fear":
        if secondmax = "anger":
            s = "Your primary emotions are anger and fear. A possible explanation is initimidation and rationalization to meet one's own needs. Speakers perceived to be angry as a protective response, as in the case of fear, is a positive outlook, however, the stimuli inducing such fear may be irrationally perceived."
        elif secondmax = "disgust":
            s = "Disgust and fear are your primary emotions. This suggests an indeterminably phobic body language and speech. "
        elif secondmax = "joy":
            s = "Your primary emotions are fear and joy. This is somewhat conflicting stimuli; fear is fight-or-flight, and joy can represent excitement. Both emotions are commonly communicable through eye movement."
        elif secondmax = "sadness":
            s = "Fear and sadness are your primary emotions, and can give an impression of lack of confidence or disinterest. Be more active and engaged during communication. There also may be an anxiety component, and over time it can become a conditioned response."
        elif secondmax = "contempt":
            s = "Fear and contempt are your primary emotions. If misinterpreted, it could communicate avoidance behavior and lack of confidence. As there is a mutual process of acceptance, we suggest you to be more open in your speech."
        elif secondmax = "surprise":
            s = "Fear and surprise are your primary emotions. While facial arrangements related to surprise can be a positive, reinforcing signal to your audience, the fear component implies an fight-or-flight response."
        elif secondmax = "neutral":
            s = "Fear and neutral are your primary emotions. Neutral is always a good thing, but fear during conversation indicates reflexive worry. Fear is also contagious through pheromones."
    elif maximum = "joy":
        if secondmax = "anger":
            s = "We detect anger and joy as your primary emotions. The joy is a positive, energetic component of communication, and it is a possiblity that the anger component represents overeagerness and encroachment. We suggest you to embrace a more passive approach."
        elif secondmax = "disgust":
            s = "Disgust and joy are your primary emotions. This is somewhat conflicting stimulus and may represent fascination. Plutchik's theory of emotion describes this as positive communication."
        elif secondmax = "sadness":
            s = "Joy and sadness are your primary emotions. This is a conflicting impression; you have tend to have widely encompassing speech patterns and volatility in facial reactions."
        elif secondmax = "fear":
            s = "Fear and sadness are your primary emotions, and can give an impression of lack of confidence or disinterest. Be more active and engaged during communication. There also may be an anxiety component, and over time it can become a conditioned response."
        elif secondmax = "contempt":
            s = "Joy and contempt are your primary emotions. Joy is the most positive emotion to associate oneself, while contempt can alienate your audience. Joy and contempt manifest themselves most recognizably in speech patterns."
        elif secondmax = "surprose":
            s = "Joy and surprise are your primary emotions. Surprise and joy imply a genuine engagement in conversing, as well as comfort and security."
        elif secondmax = "neutral":
            s = "Joy and neutral are your primary emotions. This is probably the best emotion pairing and suggests passitivity as well as engagement."
    elif maxmimum = "contempt":
        if secondmax = "anger":
            s = "Your primary emotions are anger and contempt. Assertive speaking should be for stability, not dominance. This hostile appearance may stem from an over-protective instinct."
        elif secondmax = "disgust":
            s = "Disgust and contempt are your primary emotions. This might be a slight reactive mechanism towards some unpleasant stimuli. Disgust and contempt are the most recognizable facial behaviors."
        elif secondmax = "joy":
            s = "Joy and contempt are your primary emotions. Joy is the most positive emotion to associate oneself, while contempt can alienate your audience. Joy and contempt manifest themselves most recognizably in speech patterns."
        elif secondmax = "sadness":
            s = "Your primary emotions are contempt and sadness. This is indicative from negative speech and, potentially, lack of engaging facial expressions. At least pretend you're interested, asshole."
        elif secondmax = "fear":
            s = "Fear and contempt are your primary emotions. If misinterpreted, it could communicate avoidance behavior and lack of confidence. As there is a mutual process of acceptance, we suggest you to be more open in your speech."
        elif secondmax = "surprise":
            s = "Your primary emotions are contempt and surprise. Contempt is characterized as "positive self-feeling," and its pairing with surprise can mean you are both psychologically invested as well as withdrawn. Perhaps your speech is an indication of elitist reactivity."
        elif secondmax = "neutral":
            s = "Your primary emotions are contempt and neutral. Contempt is a mixture of anger and disgust, directed toward lower-status individuals. It is one of the most recognizable facial arrangements."
    elif maximum = "sadness":
        if secondmax = "anger":
            s = "Anger and sadness are your primary signals. This combination suggests passive anger, which may result in evasivenss or subtle defeatism. This requires a more open approach to communication. If you haven’t already, open your palms and relax your shoulders."
        elif secondmax = "disgust":
            s = "Disgust and sadness are your primary emotions. While disgust implies a self-defensive reaction, sadness implies a more internal consequence. Most likely, disgust is detected from facial expressions."
        elif secondmax = "joy":
            s = "Joy and sadness are your primary emotions. This is a conflicting impression; you have tend to have widely encompassing speech patterns and volatility in facial reactions."
        elif secondmax = "fear":
            s = "Fear and sadness are your primary emotions, and can give an impression of lack of confidence or disinterest. Be more active and engaged during communication. There also may be an anxiety component, and over time it can become a conditioned response."
        elif secondmax = "surprise":
            s = "Your primary emotions portrayed are sadness and surprise. Surprise and sadness are expressed through smaller pupil size. Often, sadness is contagious and lends to empathy."
        elif secondmax = "neutral":
            s = "Your main emotive signals are sadness and neutral. Neutral is always an acceptable state, and sadness suggests an underlying belief or affectation of loss."
        elif secondmax = "contempt":
            s = "Your primary emotions are contempt and sadness. This is indicative from negative speech and, potentially, lack of engaging facial expressions. At least pretend you're interested, asshole."
    elif maximum = "surprise":
        if secondmax = "anger":
            s = "Anger and surprise are your primary emotions. They suggest an intensity to your speaking and nonverbal communication with sudden changes and hostility. Smooth your speaking cadence and facial expressions."
        elif secondmax = "disgust":
            s = "Disgust and surprise are your primary emotions. If you are exaggerating facial expression, such as eyebrow-raising and mouth contortion, it may seem offputting to your audience."
        elif secondmax = "joy":
            s = "Joy and surprise are your primary emotions. Surprise and joy imply a genuine engagement in conversing, as well as comfort and security."
        elif secondmax = "sadness":
            s = "Your primary emotions portrayed are sadness and surprise. Surprise and sadness are expressed through smaller pupil size. Often, sadness is contagious and lends to empathy."
        elif secondmax = "contempt":
            s = "Your primary emotions are contempt and surprise. Contempt is characterized as "positive self-feeling," and its pairing with surprise can mean you are both psychologically invested as well as withdrawn. Perhaps your speech is an indication of elitist reactivity."
        elif secondmax = "neutral":
            s = "Your primary emotions are surprise and neutral. This is a good emotion pairing, because surprise suggests engagement and genuine reactivity, while neutral is a passiveness that is acceptable in most situations."
        elif secondmax = "fear":
            s = "Fear and surprise are your primary emotions. While facial arrangements related to surprise can be a positive, reinforcing signal to your audience, the fear component implies an fight-or-flight response."
    elif maximum = "neutral":
        elif secondmax = "anger":
            s = "Anger and neutral are your primary emotions. Neutral suggests passitivity while the pairing with anger suggests slight exaggerative response to some provocation."
        elif secondmax = "disgust":
            s = "Disgust and neutral are your primary emotions. Disgust is an aftereffect of social conditioning and is the easiest to detect. There may be a slight exaggeration in your facial expressions."
        elif secondmax = "joy":
            s = "Joy and neutral are your primary emotions. This is probably the best emotion pairing and suggests passitivity as well as engagement."
        elif secondmax = "sadness":
            s = "Your main emotive signals are sadness and neutral. Neutral is always an acceptable state, and sadness suggests an underlying belief or affectation of loss."
        elif secondmax = "contempt":
            s = "Your primary emotions are contempt and sadness. This is indicative from negative speech and, potentially, lack of engaging facial expressions. At least pretend you're interested, asshole."
        elif secondmax = "surprise":
            s = "Your primary emotions are surprise and neutral. This is a good emotion pairing, because surprise suggests engagement and genuine reactivity, while neutral is a passiveness that is acceptable in most situations."
        elif secondmax = "fear":
            s = "Fear and neutral are your primary emotions. Neutral is always a good thing, but fear during conversation indicates reflexive worry. Fear is also contagious through pheromones."
    return s
