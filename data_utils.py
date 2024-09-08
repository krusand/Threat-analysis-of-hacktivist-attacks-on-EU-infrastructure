# this file contains sets and dictionaries of search words
eu_nordic_countries = {"austria",
                       "belgium",
                       "croatia",
                       "cyprus",
                       "czech republic",
                       "denmark",
                       "estonia",
                       "finland",
                       "france",
                       "germany",
                       "greece",
                       "hungary",
                       "iceland",
                       "ireland",
                       "italy",
                       "latvia",
                       "lithuania",
                       "luxembourg",
                       "malta",
                       "netherlands",
                       "norway",
                       "poland",
                       "portugal",
                       "romania",
                       "slovakia",
                       "slovenia",
                       "spain",
                       "sweden"
                       }


sectors_patterns = {
    'energy': r'\b(energy|power|electricity|gas|oil|renewable|solar|wind|nuclear)\b',
    'transport': r'\b(transport|transportation|logistics|shipping|rail|aviation|fleet|freight|trucking)\b',
    'banking': r'\b(bank|banking|financial institution|credit|loan|mortgage|savings|investment)\b',
    'financial market infrastructure': r'\b(financial market|market infrastructure|clearing|settlement|exchange|trading platform|depository)\b',
    'health': r'\b(health|medical|hospital|clinic|pharma|biotech|healthcare|diagnostics)\b',
    'drinking water': r'\b(drinking water|potable water|water supply|water treatment|water purification)\b',
    'waste water': r'\b(waste water|sewage|wastewater|effluent|sewage treatment)\b',
    'digital infrastructure': r'\b(digital infrastructure|IT infrastructure|data center|cloud computing|networking|cybersecurity)\b',
    'public administration': r'\b(public administration|government|municipal|local authority|public sector)\b',
    'space': r'\b(space|aerospace|satellite|rocket|space agency|astronautics)\b',
    'food': r'\b(food|agriculture|food production|food processing|beverage|restaurant|catering)\b',
}


cia_principles_patterns = {
    'confidentiality': r'\b(confidentiality|privacy|unauthorized access|data breach|leak|disclosure|exposure)\b',
    'integrity': r'\b(integrity|tampering|alteration|modification|manipulation|forgery|data corruption|unauthorized changes)\b',
    'availability': r'\b(availability|downtime|outage|denial of service|DDoS|disruption|service disruption|system failure)\b',
}
