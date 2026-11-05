#!/usr/bin/env python3
"""Build the Phantom Lake Club preview: Home, Hours (the pool schedule), Water Polo and Swim Team, in the look of
phantomlakeclub.org, with every session, rental and closure read live from Pool Relay by finder.js.

Nothing about WHEN the pool is open is typed here: only prices, ages, program descriptions and facts about the water.
The club's own schedule text appears only as labeled quotes.
Run: python3 build.py   (then python3 check.py)"""
import hashlib, html

E = html.escape
LANES = "92it6ldSSl4pteiXEFcD7Y"  # Pool Relay tab: Phantom Lake Club pool, lane by lane (day)
WEEK = "NW5jUspT0J4R0HAbaQkeaC"   # Pool Relay tab: Phantom Lake Club pool, week (every booking; feeds the live text)
PL = "https://phantomlakeclub.org"
NWPC_SITE = "https://psmoore.github.io/pool_nwwaterpolo/"
FAC = "Phantom Lake Club"
CLUB = "grp:phantom-lake-club-programs"
NWPC = "grp:northwest-water-polo-club"
VER = hashlib.sha1((open("finder.js").read() + open("style.css").read()).encode()).hexdigest()[:8]

NAV = [("About", PL + "/about"), ("Hours", "hours.html"), ("Backyard", PL + "/backyard"), ("Swim Lessons", PL + "/lessons"),
       ("Swim Team", "swim-team.html"), ("Water Polo", "water-polo.html"), ("Membership", PL + "/membership"),
       ("Rentals and Parties", PL + "/rentals-and-parties"), ("Employment", PL + "/employment")]


def out(href, label, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{E(href)}" target="_blank" rel="noopener noreferrer">{label}</a>'


def live(mode, token=WEEK, **kw):
    attrs = "".join(f' data-{k.replace("_", "-")}="{E(str(v))}"' if v is not True else f' data-{k.replace("_", "-")}' for k, v in kw.items())
    return f'data-live="{mode}" data-view="{token}"{attrs}'


def frame(token, title, height=760):
    return (f'<div class="frame"><iframe src="https://www.poolrelay.com/embed/{token}" height="{height}" title="{E(title)}" '
            f'loading="lazy"></iframe></div><p class="credit">Schedule by {out("https://www.poolrelay.com/", "Pool Relay")}</p>')


def quote(lines, src, label, who="Phantom Lake Club's own text"):
    return (f'<blockquote class="quote"><span class="qh">{E(who)}, quoted from {out(src, label)}</span>'
            + "".join(f"<p>{E(l)}</p>" for l in lines) + "</blockquote>")


def link(label, href, here):
    if href.startswith("http"):
        return out(href, E(label))
    cls = ' class="here"' if href == here else ""
    return f'<a href="{href}"{cls}>{E(label)}</a>'


LIVE = '<span class="live-tag">Live</span>'


def page(file, title, body):
    nav = "".join(link(l, h, file) for l, h in NAV)
    doc = f"""<!doctype html>
<!-- UNOFFICIAL PREVIEW. Not a Phantom Lake Club website. A mock-up of {PL}
     with the pool schedule on live Pool Relay calendars. Built to demonstrate Pool Relay; not affiliated with Phantom Lake Club. -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{E(title)} — Phantom Lake Club (unofficial preview)</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Narrow:wght@400;600;700&family=Bodoni+Moda:opsz,wght@6..96,400;6..96,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={VER}">
</head>
<body>
<div class="preview-note"><b>Unofficial preview — not a Phantom Lake Club website.</b> A mock-up of {out(PL, "phantomlakeclub.org")} with its pool schedule on live {out("https://www.poolrelay.com/", "Pool Relay")} calendars.</div>
<div class="annc">We are closed for the season. Membership registrations will open soon. {out("https://phantomlake.membersplash.com/membership/join/", "Sign up now to get on our waitlist!")}</div>
<header class="site"><div class="in">
  <a class="brand" href="index.html">Phantom Lake Club</a>
  <nav class="main" aria-label="Main">{nav}</nav>
  {out("https://phantomlake.membersplash.com/membership/join/", "Join our Waitlist", "pillbtn")}
  <details class="mnav"><summary>Menu</summary><div class="mpanel">{nav}</div></details>
</div></header>
<main>
{body}
</main>
<footer>
  <div class="cols">
    <div><p class="serif" style="font-size:24px;color:#fff;margin:0 0 6px">Phantom Lake Club</p>
      <p style="margin:0">15810 SE 24th St, Bellevue, WA 98008<br>(425) 747-0260<br>{out(PL + "/contact_form", "Contact us")} · {out(PL + "/pool-rules", "Pool Rules")}</p></div>
    <div><p style="color:#fff;margin:0 0 6px"><b>In the pool today</b> {LIVE}</p><div {live("today", empty="Nothing on the schedule.")}>…</div></div>
  </div>
  <p class="disc"><b>Unofficial preview.</b> Built to demonstrate embedded {out("https://www.poolrelay.com/", "Pool Relay")} schedules. Not operated by,
    endorsed by or affiliated with Phantom Lake Club or Northwest Water Polo Club. The club's sessions were entered from its public
    Google Calendars (PLC Pool Calendar; Lessons and programs) on {out(PL + "/hours", "phantomlakeclub.org/hours")}; Northwest Water Polo Club's
    practices from that club's published schedule. Neither publishes lanes, so lane assignments are Pool Relay's estimate.
    Prices and program details are copied from {out(PL, "phantomlakeclub.org")}, which remains the official source. No Phantom Lake Club logo or photos are used.</p>
</footer>
<script src="finder.js?v={VER}"></script>
</body>
</html>
"""
    open(file, "w").write(doc)


BA = f"""<div class="ba">
  <div><h3>Today on phantomlakeclub.org</h3><ul>
    <li>The Hours page is four Google Calendars layered in week mode: pool, lessons and programs, team, social.</li>
    <li>The off-season shows nothing, though the pool is booked most weeknights by Northwest Water Polo Club.</li>
    <li>Program pages type their dates and times by hand, separately from the calendars.</li></ul></div>
  <div class="a"><h3>In this preview</h3><ul>
    <li>One schedule for the pool, drawn lane by lane: members' swims, clinics and renters side by side.</li>
    <li>Every hour on every page is read from that schedule, so a change shows up everywhere at once.</li>
    <li>The renter keeps its own practices in the same calendar, so the club sees them without asking; see the
      {out(NWPC_SITE, "Northwest Water Polo Club preview")}.</li>
    <li>Members can follow a program from the calendar's filter row and get an email when it changes.</li></ul></div>
</div>"""

# ── Home ─────────────────────────────────────────────────────────────────────
page("index.html", "Join and experience summer fun", f"""
<section class="hero"><div><h1>Phantom Lake Club</h1>
  <p class="lede">A member-owned club on the shores of Phantom Lake in east Bellevue: a six-lane, 25-yard competition pool with a dive board.</p>
  <p style="margin-top:18px"><a class="btn ghost" href="hours.html">Pool schedule</a></p></div></section>
<section class="band purple"><div class="wrap">
  <p class="big serif">We are closed for the members' season</p>
  <p class="center">Membership registrations for next summer open soon. {out("https://phantomlake.membersplash.com/membership/join/", "Join the waitlist")}.</p>
  <div class="cols" style="margin-top:26px">
    <div class="card"><h3>In the pool today {LIVE}</h3><div {live("today", empty="Nothing on the schedule.")}>…</div></div>
    <div class="card"><h3>Off-season renter {LIVE}</h3>
      <p class="small" style="margin:0 0 6px">Northwest Water Polo Club practices here in the off-season:</p>
      <div {live("when", groups=NWPC, by_title=True, past_note="Its next session has not been entered yet.")}>…</div>
      <p class="small" style="margin:0">Published practices run <span {live("through", groups=NWPC)}>…</span>.</p></div>
  </div>
</div></section>
<section class="band"><div class="wrap">
  <h2>This week at the pool {LIVE}</h2>
  <div class="week" {live("week", skip_empty=True, empty="Nothing in the pool this week.")}><p class="muted">Loading the week…</p></div>
  <h2 style="margin-top:34px">The pool, lane by lane {LIVE}</h2>
  <p class="small muted">Six lanes, one column each. Pick a day; use the filter row to show one program. Its <b>Subscribe</b> button emails
    you when that program's schedule changes.</p>
  {frame(LANES, "Phantom Lake Club pool, lane by lane", 760)}
</div></section>
<section class="band tint"><div class="wrap">
  <h2>What's different in this preview</h2>
  {BA}
</div></section>
""")

# ── Hours ────────────────────────────────────────────────────────────────────
page("hours.html", "Hours", f"""
<div class="pagehead"><h1>Pool schedule</h1></div>
<section class="band" style="padding-top:10px"><div class="wrap">
  <div class="cols">
    <div><h3>Today {LIVE}</h3><div {live("today", empty="Nothing on the schedule.")}>…</div></div>
    <div><h3>Closures {LIVE}</h3><div {live("closures", ahead=120)}></div>
      <p class="small muted">Closures entered on the pool appear here and clear those hours from every list on the site.</p></div>
  </div>
  <h2 style="margin-top:28px">The week {LIVE}</h2>
  <div class="week" {live("week", empty="Nothing in the pool this week.")}><p class="muted">Loading the week…</p></div>
  <h2 style="margin-top:34px">Week view {LIVE}</h2>
  {frame(WEEK, "Phantom Lake Club pool, week", 780)}
  <h2 style="margin-top:34px">Lane by lane {LIVE}</h2>
  {frame(LANES, "Phantom Lake Club pool, lane by lane", 760)}
  <h3>Members' sessions at the end of the season {LIVE}</h3>
  <div {live("when", groups=CLUB, by_title=True, lookback=60, past_note="The members' season is over.")}>…</div>
  {quote(["We are currently closed. Our summer season starts in May and ends in September. Check the calendar at a later point for details"],
         PL + "/hours", "Hours")}
</div></section>
""")

# ── Water Polo ───────────────────────────────────────────────────────────────
page("water-polo.html", "Water Polo", f"""
<div class="pagehead"><h1>Water Polo Team</h1>
  <p class="subnav"><a href="#about">About</a> | <a href="#renters">Off-season</a> | {out(PL + "/water-polo", "Practice Schedule")} | {out(PL + "/water-polo", "Registration")}</p></div>
<section class="band" id="about"><div class="wrap cols">
  <div><h2>About</h2>
    <p>Join the exciting and fast-growing sport of water polo! Phantom Lake Water Polo is a summer league team sponsored by PLC under the
      umbrella of the Midlakes Water Polo League, a recreational league that emphasizes sportsmanship, education, skill development, and
      participation through friendly competition. PLC is one of 14 teams in Midlakes Water Polo.</p>
    <p>Water polo is open to all members. There are no tryouts, and all are welcome regardless of experience or ability. Teams are coed
      and compete against like-aged opponents: 10 and under, 12 and under, 14 and under, and 15 and up.</p></div>
  <div><ul class="facts"><li><b>Team fee:</b> $128 per player</li><li><b>Who:</b> PLC members, or members of another Midlakes pool without a water polo team</li>
    <li><b>Required:</b> Midlakes Hold Harmless Agreement, concussion form, U.S. Center for SafeSport training</li></ul>
    <p class="small muted">The summer team's practice and game times will be entered on the pool calendar when the season is set.</p></div>
</div></section>
<section class="band purple" id="renters"><div class="wrap">
  <h2>Off-season water polo at Phantom Lake {LIVE}</h2>
  <p>Northwest Water Polo Club, a year-round club, trains here in the off-season. Its practices are on the same pool calendar, lane by lane,
    entered by the club itself:</p>
  <div class="card"><div {live("when", groups=NWPC, by_title=True, past_note="Its next session has not been entered yet.")}>…</div>
    <p class="small" style="margin:0">Next: <span {live("next", groups=NWPC, show_title=True)}>…</span></p></div>
  <p class="small" style="margin-top:12px">{out(NWPC_SITE, "Northwest Water Polo Club (preview)")}</p>
</div></section>
<section class="band"><div class="wrap">
  <h2>Pool calendar {LIVE}</h2>
  {frame(WEEK, "Phantom Lake Club pool, week", 780)}
</div></section>
""")

# ── Swim Team ────────────────────────────────────────────────────────────────
page("swim-team.html", "Swim Team", f"""
<div class="pagehead"><h1>Swim Team</h1></div>
<section class="band"><div class="wrap cols">
  <div><h2>Swim Team Only Weekend Skills Practice</h2>
    <p>Keep skills sharp and stay connected heading into the off-season. Each session is limited to 18 swimmers, and spots tend to fill quickly.</p>
    <ul class="facts"><li><b>Price:</b> $12 per session or $50 for all five clinics</li><li><b>Groups:</b> 8U &amp; 10U, then 12U &amp; 13+</li>
      <li><b>Register:</b> {out("https://phantomlake.membersplash.com/swimclinic/", "Membersplash, under swim clinics")} (members log in)</li></ul></div>
  <div class="card"><h3>Clinic times {LIVE}</h3>
    <div {live("when", groups="grp:swim-team-clinics", by_title=True, lookback=60, past_note="This year's clinics are over.")}>…</div></div>
</div></section>
<section class="band tint"><div class="wrap">
  <h2>About Phantom Lake Swim Team</h2>
  <p>A recreational summer swim program focused on skill development, teamwork, and fun. Swimmers practice through the season and compete
    in age-group races against other Midlakes Swim League teams. All ability levels are welcome and there are no tryouts; swimmers should be
    able to swim across the width of the pool (about 42 feet).</p>
  <ul class="facts"><li><b>Team fee:</b> $255 per swimmer, plus the $16.80 annual Swimmingly fee</li>
    <li><b>Mini Phantoms</b> (age 4+, comfortable in the water but not yet swimming 25 yards): $100 per swimmer</li></ul>
  {quote(["Season runs from May 18th to July 28th."], PL + "/swim-team", "Swim Team")}
  <p class="small muted">Next summer's practice times will read from the pool calendar once entered.</p>
</div></section>
""")
print("built 4 pages")
