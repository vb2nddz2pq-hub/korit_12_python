logo = r'''
.------..------..------..------..------..------..------.
|H.--. ||A.--. ||N.--. ||G.--. ||M.--. ||A.--. ||N.--. |
| :/\: || (\/) || :(): || :/\: || (\/) || (\/) || :(): |
| (__) || :\/: || ()() || :\/: || :\/: || :\/: || ()() |
| '--'H|| '--'A|| '--'N|| '--'G|| '--'M|| '--'A|| '--'N|
`------'`------'`------'`------'`------'`------'`------'
'''

print(logo)

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


words = [
    "ability", "absence", "academy", "account", "accused", "achieve", "acquire", "address", "advance", "adverse",
    "advised", "adviser", "against", "airline", "airport", "alcohol", "alleged", "already", "analyst", "ancient",
    "another", "anxiety", "anybody", "applied", "arrange", "arrival", "article", "assault", "assumed", "assured",
    "attempt", "attract", "auction", "average", "backing", "balance", "banking", "barrier", "battery", "bearing",
    "beating", "because", "bedroom", "believe", "beneath", "benefit", "besides", "between", "billion", "binding",
    "brother", "brought", "burning", "cabinet", "caliber", "calling", "capable", "capital", "captain", "caption",
    "capture", "careful", "carrier", "caution", "ceiling", "central", "certain", "chamber", "channel", "chapter",
    "charity", "charlie", "charter", "checked", "chicken", "chronic", "circuit", "classes", "classic", "cleaner",
    "clearly", "closing", "closure", "collect", "college", "combine", "comfort", "command", "comment", "compact",
    "company", "compare", "compete", "complex", "concept", "concern", "concert", "conduct", "confirm", "connect",
    "consent", "consist", "contact", "contain", "content", "contest", "context", "control", "convert", "correct",
    "council", "counsel", "counter", "country", "crucial", "crystal", "culture", "current", "cutting", "damaged",
    "dealing", "decided", "decline", "default", "defence", "deficit", "deliver", "density", "deposit", "desktop",
    "despite", "destroy", "develop", "devoted", "diamond", "digital", "discuss", "disease", "display", "dispute",
    "distant", "diverse", "divided", "drawing", "driving", "dynamic", "economy", "edition", "effects", "efforts",
    "eighty", "element", "engaged", "engine", "enjoyed", "enormous", "entered", "entire", "entity", "episode",
    "equally", "evening", "evident", "exactly", "examine", "example", "excited", "exclude", "exhibit", "expense",
    "explain", "explore", "express", "extreme", "factory", "faculty", "failing", "failure", "fashion", "feature",
    "federal", "feeling", "fiction", "fifteen", "finally", "finance", "finding", "fishing", "fitness", "foreign",
    "forever", "formula", "fortune", "forward", "founder", "freedom", "further", "gallery", "gateway", "general",
    "genuine", "getting", "glasses", "greater", "growing", "handled", "hanging", "happens", "healthy", "hearing",
    "heavily", "helpful", "heritage", "history", "holding", "holiday", "housing", "however", "hundred", "husband",
    "identity", "imagine", "impact", "improve", "include", "income", "increase", "indeed", "index", "indicate",
    "infant", "inform", "injury", "inside", "insight", "install", "instant", "instead", "intense", "interim",
    "invest", "involve", "island", "itself", "jacket", "journey", "justice", "keeping", "killed", "kitchen",
    "knowing", "labour", "ladder", "landing", "largely", "latest", "launch", "lawyer", "leader", "leading",
    "learning", "leather", "legacy", "legend", "length", "lesson", "letter", "liberal", "library", "license",
    "limited", "listing", "logical", "loyal", "machine", "magazine", "mainly", "maintain", "manager", "manner",
    "market", "married", "massive", "master", "matrix", "maximum", "meaning", "measure", "medical", "meeting",
    "member", "memory", "mental", "mention", "message", "million", "mineral", "minimal", "minimum", "missing",
    "mission", "mistake", "mixture", "mobile", "modern", "moment", "money", "monitor", "monthly", "morning",
    "mostly", "mother", "motion", "mountain", "movement", "multiple", "museum", "music", "musical", "mutual",
    "myself", "narrow", "nation", "native", "natural", "nature", "nearby", "nearly", "network", "neutral",
    "nobody", "normal", "notice", "notion", "nuclear", "number", "object", "obvious", "offense", "officer",
    "ongoing", "opening", "operate", "opinion", "optical", "option", "orange", "order", "ordinary", "organic",
    "outcome", "outdoor", "outside", "overall", "package", "painted", "parking", "partial", "partner", "passage",
    "passing", "passion", "passive", "patient", "pattern", "payment", "penalty", "pending", "pension", "people",
    "perfect", "perform", "perhaps", "period", "permit", "person", "phrase", "physics", "picture", "plastic",
    "player", "please", "pocket", "police", "policy", "portion", "poverty", "precisely", "predict", "premier",
    "prepare", "present", "prevent", "pricing", "primary", "printer", "privacy", "private", "problem", "proceed",
    "process", "produce", "product", "profile", "program", "project", "promise", "promote", "proper", "protect",
    "protein", "protest", "provide", "publish", "purpose", "pushing", "quality", "quarter", "quickly", "quietly",
    "radical", "railway", "raising", "random", "rapidly", "rather", "rating", "reader", "reality", "realize",
    "reason", "receive", "recent", "record", "reduced", "reflect", "reform", "refuse", "regard", "regime",
    "region", "regular", "related", "relief", "remain", "remote", "removal", "repair", "replace", "report",
    "request", "reserve", "resolve", "respect", "restore", "result", "retail", "retain", "return", "reveal",
    "review", "reward", "riding", "rising", "robust", "rolling", "roughly", "running", "safety", "salary",
    "sample", "saving", "scandal", "scheme", "school", "science", "screen", "search", "season", "second",
    "secret", "sector", "secure", "seeing", "select", "seller", "senior", "sensor", "series", "service",
    "session", "setting", "settle", "seven", "several", "shaking", "shared", "sharp", "sheet", "shelf",
    "shell", "shift", "shipping", "shock", "shooting", "shopping", "short", "should", "showing", "shower",
    "sight", "signal", "silent", "silver", "similar", "simple", "simply", "since", "single", "sister",
    "site", "situated", "sixth", "size", "skill", "sleep", "slight", "slowly", "small", "smart",
    "smile", "smoke", "smooth", "social", "society", "soft", "software", "soil", "solar", "solid",
    "solve", "some", "somebody", "somehow", "someone", "something", "sometime", "somewhat", "song", "soon"
]