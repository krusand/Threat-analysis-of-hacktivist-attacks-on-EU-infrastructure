# this file contains sets and dictionaries of search words
eu_nordic_countries = {"at": "austria",
                       "be": "belgium",
                       "hr": "croatia",
                       "cy": "cyprus",
                       "cz": "czech republic",
                       "dk": "denmark",
                       "ee": "estonia",
                       "fi": "finland",
                       "fr": "france",
                       "de": "germany",
                       "gr": "greece",
                       "hu": "hungary",
                       "is": "iceland",
                       "ie": "ireland",
                       "it": "italy",
                       "lv": "latvia",
                       "lt": "lithuania",
                       "lu": "luxembourg",
                       "mt": "malta",
                       "nl": "netherlands",
                       "no": "norway",
                       "pl": "poland",
                       "pt": "portugal",
                       "ro": "romania",
                       "sk": "slovakia",
                       "si": "slovenia",
                       "es": "spain",
                       "se": "sweden"
                       }


sectors_patterns = {
    'energy': r'\b(energy|power|electricity|gas|oil|renewable|solar|wind|nuclear)',
    'transport': r'\b(transport|transportation|logistics|shipping|rail|aviation|fleet|freight|trucking|airport|airplane|railway)',
    'banking': r'\b(bank|banking|financial institution|credit|loan|mortgage|savings|investment|finance)',
    'financial market infrastructure': r'\b(financial market|financial|market infrastructure|clearing|settlement|exchange|trading platform|depository)',
    'health': r'\b(health|medical|hospital|clinic|pharma|biotech|healthcare|diagnostics)',
    'drinking water': r'\b(drinking water|potable water|water supply|water treatment|water purification)',
    'waste water': r'\b(waste water|sewage|wastewater|effluent|sewage treatment)',
    'digital infrastructure': r'\b(digital infrastructure|IT infrastructure|data center|cloud computing|networking|cybersecurity|tele|cloud)',
    'public administration': r'\b(public administration|government|municipal|local authority|public sector|ministry|committee|council|court)',
    'space': r'\b(space|aerospace|satellite|rocket|space agency|astronautics)',
    'food': r'\b(food|agriculture|food production|food processing|beverage|restaurant|catering)',
}


cia_principles_patterns = {
    'confidentiality': r'\b(confidentiality|privacy|unauthorized access|data breach|leak|disclosure|exposure)\b',
    'integrity': r'\b(integrity|tampering|alteration|modification|manipulation|forgery|data corruption|unauthorized changes)\b',
    'availability': r'\b(availability|downtime|outage|denial of service|DDoS|disruption|service disruption|system failure)\b',
}
