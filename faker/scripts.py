from faker import Faker
from faker.providers import DynamicProvider
from math import floor
from datetime import timedelta, datetime
import random as rand

# Config
seed = 3394
base_data_amount = 20
other_data_amount = 50
file_name = "FormulaNone1.sql"

# Faker and Random initialization
rand.seed(seed)
Faker.seed(seed)
fake = Faker()
fake_div = Faker(['en_AU', 'de_LI', 'de_LU', 'es_AR', 'fr_BE'])


team_name_provider = DynamicProvider(
    provider_name='team_name',
    elements=["Alpine",
    "Aston Martin",
    "Audi",
    "Cadillac",
    "Ferrari",
    "Haas",
    "McLaren",
    "Mercedes",
    "Racing Bulls",
    "Red Bull Racing",
    "Williams",
    "Alex von Falkenhausen Motorenbau",
    "Automobiles Gonfaronnaises Sportives",
    "Alfa Romeo",
    "Alfa Special",
    "AlphaTauri",
    "Alta",
    "Amon",
    "Andrea Moda",
    "Apollon",
    "Arrows",
    "Arzani-Volpini",
    "Aston Butterworth",
    "Automobili Turismo e Sport",
    "Auto Technisches Spezialzubehor",
    "British American Racing",
    "Behra-Porsche",
    "Bellasi",
    "Benetton",
    "Boro",
    "Brabham",
    "Brawn GP",
    "British Racing Motors",
    "British Racing Partnership",
    "Bugatti",
    "Caterham",
    "Cisitalia",
    "Coloni",
    "Connaught",
    "Connew",
    "Cooper Car Company",
    "Dallara",
    "De Tomaso",
    "Eagle",
    "Eifelland",
    "Emeryson",
    "Eisenacher Motorenwerk",
    "Ecurie Nationale Belge",
    "Ensign",
    "English Racing Automobiles",
    "EuroBrun",
    "Ferguson Research Ltd.",
    "FIRST",
    "Fittipaldi Automotive",
    "Fondmetal",
    "Force India",
    "Forti",
    "Frank Williams Racing Cars",
    "Frazer-Nash",
    "Fry",
    "Gilby Engineering",
    "Gordini",
    "Greifzu",
    "Hesketh",
    "Hill",
    "Hispania Racing Team",
    "Honda",
    "Hersham and Walton Motors",
    "Jaguar",
    "JBW",
    "Jordan",
    "Kauhsen",
    "Klenk",
    "Kojima",
    "Kurtis Kraft",
    "Lambo",
    "Lancia",
    "Larrousse",
    "LDS",
    "LEC",
    "Leyton House",
    "Life",
    "Ligier/Talbot Ligier",
    "Lola",
    "Lotus",
    "Lyncar",
    "Maki",
    "Manor",
    "March",
    "Martini",
    "Marussia",
    "Maserati",
    "Matra",
    "MBM",
    "McGuire",
    "Merzario",
    "Midland",
    "Milano",
    "Minardi",
    "Onyx",
    "O.S.C.A.",
    "Osella",
    "Pacific",
    "Parnelli",
    "Penske",
    "Porsche",
    "Prost",
    "RAM",
    "Racing Point Force India",
    "Racing Point",
    "RE",
    "Renault",
    "Rebaque",
    "Rial",
    "Sauber/BMW Sauber/Kick Sauber",
    "Scarab",
    "Scirocco",
    "Shadow",
    "Shannon",
    "Simca-Gordini",
    "Simtek",
    "Spirit",
    "Spyker",
    "Stebro",
    "Stewart",
    "Super Aguri",
    "Surtees",
    "SVA",
    "Talbot-Lago",
    "Tec-Mec",
    "Tecno",
    "Theodore",
    "Token",
    "Toleman",
    "Toro Rosso",
    "Toyota",
    "Trojan",
    "Tyrrell",
    "Vanwall",
    "Venturi",
    "Veritas",
    "Virgin",
    "Walter Wolf Racing",
    "Zakspeed"]
)

circuit_name_provider = DynamicProvider(
    provider_name='circuit_name',
    elements=["Adelaide Street Circuit",
    "Ain-Diab Circuit",
    "Aintree Motor Racing Circuit",
    "Albert Park Circuit",
    "Algarve International Circuit",
    "Autodromo do Estoril",
    "Autodromo Hermanos Rodriguez",
    "Autodromo Internacional Nelson Piquet",
    "Autodromo Internazionale del Mugello",
    "Autodromo Internazionale Enzo e Dino Ferrari",
    "Autodromo Jose Carlos Pace",
    "Autodromo Nazionale di Monza",
    "Autodromo Oscar y Juan Galvez",
    "AVUS",
    "Bahrain International Circuit",
    "Baku City Circuit",
    "Brands Hatch Circuit",
    "Buddh International Circuit",
    "Bugatti Circuit",
    "Caesars Palace Grand Prix Circuit",
    "Circuit Bremgarten",
    "Circuit de Barcelona-Catalunya",
    "Circuit de Charade",
    "Circuit de Monaco",
    "Circuit de Nevers Magny-Cours",
    "Circuit de Pedralbes",
    "Circuit de Reims-Gueux",
    "Circuit de Spa-Francorchamps",
    "Circuit Dijon-Prenois",
    "Circuit Gilles Villeneuve",
    "Circuit Mont-Tremblant",
    "Circuit of the Americas",
    "Circuit Paul Ricard",
    "Circuit Zandvoort",
    "Circuit Zolder",
    "Circuito da Boavista",
    "Circuito de Monsanto",
    "Circuito Permanente de Jerez",
    "Circuito Permanente del Jarama",
    "Dallas Fair Park",
    "Detroit Street Circuit",
    "Donington Park",
    "Fuji Speedway",
    "Hockenheimring",
    "Hungaroring",
    "Indianapolis Motor Speedway",
    "Istanbul Park",
    "Jeddah Corniche Circuit",
    "Korea International Circuit",
    "Kyalami Grand Prix Circuit",
    "Las Vegas Strip Circuit",
    "Long Beach Street Circuit",
    "Lusail International Circuit",
    "Madring",
    "Marina Bay Street Circuit",
    "Miami International Autodrome",
    "Montjuic Circuit",
    "Mosport Park",
    "Nivelles-Baulers",
    "Nurburgring",
    "Pescara Circuit",
    "Phoenix Street Circuit",
    "Prince George Circuit",
    "Red Bull Ring",
    "Riverside International Raceway",
    "Rouen-Les-Essarts",
    "Scandinavian Raceway",
    "Sebring Raceway",
    "Sepang International Circuit",
    "Shanghai International Circuit",
    "Silverstone Circuit",
    "Sochi Autodrom",
    "Suzuka International Racing Course",
    "TI Circuit Aida",
    "Valencia Street Circuit",
    "Watkins Glen International",
    "Yas Marina Circuit",
    "Zeltweg Airfield"
    ]
)

supplier_name_provider = DynamicProvider(
    provider_name='supplier_name',
    elements= ["Acer",
    "Alfa Romeo",
    "Alta",
    "Arrows",
    "Asiatech",
    "Aston Martin",
    "Audi~",
    "ATS",
    "BMW",
    "Borgward",
    "BPM",
    "Bristol",
    "BRM",
    "Bugatti",
    "Butterworth",
    "BWT Mercedes",
    "Castellotti",
    "Climax",
    "Conrero",
    "Cosworth",
    "De Tomaso",
    "EMW",
    "ERA",
    "European",
    "Ferrari~",
    "Fiat",
    "Fondmetal",
    "Ford",
    "Gordini",
    "Hart",
    "Honda~",
    "Honda RBPT",
    "Ilmor",
    "Jaguar",
    "JAP",
    "Judd",
    "Küchen",
    "Lamborghini",
    "Lancia",
    "Lea-Francis",
    "Life",
    "Maserati",
    "Matra",
    "Mecachrome",
    "Megatron",
    "Mercedes~",
    "Motori Moderni",
    "Mugen-Honda",
    "OSCA",
    "Osella",
    "Petronas",
    "Peugeot",
    "Playlife",
    "Porsche",
    "Pratt & Whitney",
    "Red Bull Powertrains",
    "Red Bull Ford~",
    "Renault",
    "Repco",
    "Sauber",
    "Scarab",
    "Serenissima",
    "Subaru",
    "Supertec",
    "TAG",
    "TAG Heuer",
    "Talbot",
    "Tecno",
    "Toro Rosso",
    "Toyota",
    "Vanwall",
    "Veritas",
    "Weslake",
    "Yamaha",
    "Zakspeed"
]
)

certification_provider = DynamicProvider(
    provider_name='certification',
    elements = ['Nasional', 'Internasional']
)
specialisation_provider = DynamicProvider(
    provider_name='specialisation',
    elements=['Flag Marshal', 'Incidental Marshal', 'Observer Marshal']
)

def main():
    global base_data_amount, other_data_amount, file_name
    fake.add_provider(team_name_provider)
    fake.add_provider(circuit_name_provider)
    fake.add_provider(supplier_name_provider)
    fake.add_provider(certification_provider)
    fake.add_provider(specialisation_provider)
    generate_data(base_data_amount, other_data_amount, file_name)

# Generator Function
def generate_data(base_data_amount, other_data_amount, file_name):
    # -$ Negara Generation
    countries = [fake.unique.country() for i in range(base_data_amount)]
    countries.sort()
    countries_tuples = [(i+1, countries[i]) for i in range(len(countries))]
    countries_dict = {id : country for (id, country) in countries_tuples}
    
    # -$ Tim Generation
    team_amount = other_data_amount
    team_names = [fake.unique.team_name() for i in range(team_amount)]
    team_principles = [fake_div.unique.name() for i in range(team_amount)]
    team_budgets = [fake.random_int(500000, 3500000, 100000) for i in range(team_amount)]
    team_country_ids = generate_bag(team_amount, [c[0] for c in countries_tuples])
    team_tuples = [(i+1, team_names[i], team_principles[i], team_budgets[i], team_country_ids[i]) for i in range(team_amount)]
    teams_dict = {id : (tn, tp, tb, tcid) for (id, tn, tp, tb, tcid) in team_tuples}
    
    # -$ Sirkuit Generation
    circuit_amount = other_data_amount
    circuit_names = [fake.unique.circuit_name() for i in range(circuit_amount)]
    circuit_lengths = [fake.random_int(3340, 22844, 1) for i in range(circuit_amount)]
    circuit_turns = [fake.random_int(4, 38, 1) for i in range(circuit_amount)]
    circuit_country_ids = generate_bag(circuit_amount, [c[0] for c in countries_tuples])
    circuit_tuples = [(i+1, circuit_names[i], circuit_lengths[i], circuit_turns[i], circuit_country_ids[i]) for i in range(circuit_amount)]
    
    # -$ Musim Generation
    season_amount = base_data_amount
    season_years = [1950 + fake.unique.random_int(0, 74, 1) for i in range(season_amount)]
    season_years.sort()
    season_gp_count = [fake.random_int(4, 8, 1) for i in range(season_amount)]
    season_tuples = [(i+1, season_years[i], season_gp_count[i]) for i in range(season_amount)]
    seasons_dict = {id : (y, gpc) for (id, y, gpc) in season_tuples}
    
    # -$ GrandPrix Generation
    gp_count = sum([season_tuples[i][2] for i in range(len(season_tuples))])
    gp_circuit_ids = generate_bag(gp_count, [circuit[0] for circuit in circuit_tuples])
    circ_country_ids = [circuit_country_ids[gp_circuit_ids[i]-1] for i in range(gp_count)]
    circ_countries = [countries[country_id-1] for country_id in circ_country_ids]
    gp_season_ids = generate_bag(gp_count, [season[0] for season in season_tuples])
    gp_season_years = [season_years[n-1] for n in gp_season_ids]
    gp_names = [
        f"{circ_countries[i]} Grand Prix {gp_season_years[i]}"
        for i in range(gp_count)
    ]
    gp_dates = [str(yyyy) + '-' + fake.date(pattern='%m-%d') for yyyy in gp_season_years]
    gp_tuples = [(i + 1, gp_names[i], gp_dates[i], gp_season_ids[i], gp_circuit_ids[i]) for i in range(gp_count)]
    gp_dict = {id : (n, d, sid, cid) for (id, n, d, sid, cid) in gp_tuples}
    years = [v[0] for v in list(seasons_dict.values())]
    
    # -$ Sesi Generation
    session_count = gp_count * 4
    session_gp_ids = [gp_id for gp_id in list(gp_dict.keys()) for _ in range(4)]
    session_types = []

    for _ in range(gp_count):
        session_types.extend([
            'Latihan Bebas',
            'Kualifikasi',
            'Sprint',
            'Balapan Utama'
        ])

    session_dates = []
    session_offsets = {
        'Latihan Bebas': -2,
        'Kualifikasi': -1,
        'Sprint': 0,
        'Balapan Utama': 1
    }

    for i in range(session_count):
        gp_id = session_gp_ids[i]
        gp_date = gp_dict[gp_id][1]

        session_type = session_types[i]

        gp_datetime = datetime.strptime(gp_date, "%Y-%m-%d")

        offset = session_offsets[session_type]

        session_date = (
            gp_datetime + timedelta(days=offset)
        ).strftime('%Y-%m-%d')

        session_dates.append(session_date)

    session_tuples = [(i+1, session_gp_ids[i], session_types[i], session_dates[i]) for i in range(session_count)]
    sessions_dict = {id : (gpid, t, d) for (id, gpid, t, d) in session_tuples}

    # -$ Marshal Generation
    marshal_count = base_data_amount
    marshal_names = [fake_div.name() for _ in range(marshal_count)]
    marshal_certs = [fake.certification() for _ in range(marshal_count)]
    marshal_tuples = [(i+1, marshal_names[i], marshal_certs[i]) for i in range(marshal_count)]

    # -$ Specialisation Generation
    specialisation_amounts = [fake.random_int(0, 3, 1) for _ in range(marshal_count)]
    specialisation_tuples = []
    for i in range(marshal_count):
        fake.unique.clear()
        marshal_id = marshal_tuples[i][0]
        n = specialisation_amounts[i]
        specialisations = [fake.unique.specialisation() for _ in range(n)]
        specialisation_tuples.extend([(marshal_id, spec) for spec in specialisations])

    # -$ Mengawasi Generation 
    observes_tuples = []
    marshal_ids = [m[0] for m in marshal_tuples]
    for s_id in list(sessions_dict.keys()):
        m_id = rand.choice(marshal_ids)
        gp_id = sessions_dict[s_id][0]
        observes_tuples.append((m_id, s_id, gp_id))

    # -$ Supplier_Mesin Generation
    supplier_count = base_data_amount
    supplier_names = [fake.unique.supplier_name() for i in range(supplier_count)]
    supplier_tuples = [(i+1, supplier_names[i]) for i in range(supplier_count)]
    suppliers_dict = {id : n for (id, n) in supplier_tuples}

    # -$ Pembalap Generation
    racer_count =  floor(other_data_amount * 1.5)
    racer_names = [fake_div.name() for _ in range(racer_count)]
    racer_numbers = [fake.unique.random_int(1, 99, 1) for _ in range(racer_count)]
    racer_points = [0 for _ in range(racer_count)]
    racer_country_ids = generate_bag(racer_count, list(countries_dict.keys()))
    racer_tuples = [(i+1, racer_names[i], racer_numbers[i], racer_points[i], racer_country_ids[i]) for i in range(racer_count)]
    racers_dict = {id : (n, num, p, cid) for (id, n, num, p, cid) in racer_tuples}

    
    # -$ Kontrak Generation
    teams_per_season = 22
    contract_count = teams_per_season * season_amount
    contract_racer_ids = []
    contract_team_ids = generate_bag(contract_count, list(teams_dict))
    contract_season_ids = [sid for sid in list(seasons_dict.keys()) for _ in range(teams_per_season)]
    contract_years = []
    # -$ Pembalap_Aktif dan Pembalap_Pensiun Generation
    active_racer_count = max(other_data_amount, teams_per_season)
    active_racer_ids = sorted(generate_bag(active_racer_count, list(racers_dict.keys())))
    debut_years = [fake.random_int(min(years), max(years), 1) for _ in range(active_racer_count)]
    active_contract_status = ['Tidak Aktif' for _ in range(active_racer_count)]
    active_racer_tuples = [(active_racer_ids[i], debut_years[i], active_contract_status[i]) for i in range(active_racer_count)]
    active_racers_dict = {id : (y, cs) for (id, y, cs) in active_racer_tuples}

    retired_count = racer_count - active_racer_count
    retired_ids = sorted([id for id in list(racers_dict.keys()) if id not in active_racer_ids])
    retired_years = [fake.random_int(min(years), max(years), 1) for _ in range(retired_count)]
    retired_total_participation = [0 for _ in range(retired_count)]
    retired_tuples = [(retired_ids[i], retired_years[i], retired_total_participation[i]) for i in range(retired_count)]
    retired_dict = {id : (y, tp) for (id, y, tp) in retired_tuples}
    # Pembalap algo
    current_year = 0
    valid_racer_ids = []
    for i in range(contract_count):
        contract_sid = contract_season_ids[i]
        contract_year = seasons_dict[contract_sid][0]
        if current_year != contract_year: 
            valid_racer_ids = [id for id in list(active_racers_dict.keys()) if contract_year >= active_racers_dict[id][0]]
            valid_retirees = [id for id in list(retired_dict.keys()) if contract_year <= retired_dict[id][0]]
            valid_racer_ids.extend(valid_retirees)
            current_year = contract_year

        if len(valid_racer_ids) < teams_per_season:
            valid_racer_ids = list(racers_dict.keys())[:]

        racer_id = valid_racer_ids.pop(rand.randint(0, len(valid_racer_ids)-1))
        contract_racer_ids.append(racer_id)
        contract_years.append(contract_year)
    contract_tuples = [(contract_racer_ids[i], contract_team_ids[i], contract_season_ids[i], contract_years[i]) for i in range(contract_count)]

    # -$ Memasok Generation
    supplies_set = set()

    for contract in contract_tuples:
        supplier_id = rand.choice(list(suppliers_dict.keys()))
        supplies_entry = (supplier_id, contract[1], contract[2])
        supplies_set.add(supplies_entry)

    supplies_tuples = list(supplies_set)

    # go through each contract and pick a random supplier from the list :thumbs_up: 

    # -$ Berpartisipasi_di Generation
    points_arr = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1] 
    players_per_race = min(22, racer_count)
    participation_count = gp_count * players_per_race
    participant_ids = []
    participation_gp_ids = []
    participant_placements = []
    participant_times = []
    participant_points = []
    for gp_id in gp_dict.keys():
        prev_time = fake.pyfloat(right_digits=2, min_value=4800, max_value=7200)
        selected_racers = rand.sample(list(racers_dict.keys()), players_per_race)
        participant_ids.extend(selected_racers)
        participation_gp_ids.extend([gp_id for _ in range(players_per_race)])
        participant_placements.extend([i+1 for i in range(players_per_race)])
        for n in range(players_per_race):
            difference = fake.pyfloat(right_digits=2, min_value=1, max_value=7)
            time_value = prev_time + difference

            hours = int(time_value // 3600)
            minutes = int((time_value % 3600) // 60)
            seconds = time_value % 60

            formatted_time = f"{hours:02}:{minutes:02}:{seconds:05.2f}"

            participant_times.append(formatted_time)
            prev_time += difference
            points_gained = 0
            if n < len(points_arr): 
                points_gained = points_arr[n]
                participant_points.append(points_gained)
            else: participant_points.append(0)
    
    # Calculate points for each racer
    for i in range(participation_count):
        points = participant_points[i]
        racer_id = participant_ids[i]
        racer_data  = racers_dict[racer_id]
        racers_dict[racer_id] = (racer_data[0], racer_data[1], racer_data[2] + points, racer_data[3])
    racer_tuples = [(k, v[0], v[1], v[2], v[3]) for (k, v) in zip(list(racers_dict.keys()), list(racers_dict.values()))] # update racer tuple
    
    participation_tuples = [(participant_ids[i], participation_gp_ids[i], participant_placements[i], participant_times[i], participant_points[i]) for i in range(participation_count)]
    # participation_dict = {id : (rid, gpid, p, t, pts) for (id, rid, gpid, p, t, pts) in participation_tuples}


    # Calculate total races for retired racers
    new_retired_tuples = []
    for racer_data in retired_tuples:
        r_id = racer_data[0]
        races_count = len([v for v in participation_tuples if v[0] == r_id])
        new_data = (r_id, racer_data[1], races_count)
        new_retired_tuples.append(new_data)
    retired_tuples = new_retired_tuples
    retired_dict = {id : (y, tp) for (id, y, tp) in retired_tuples} # updates retired dict

    # Determine contract status for active racers
    # Asumsi kontrak aktif selama 1 musim/tahun
    active_year = max(years)
    active_contracts = [c for c in contract_tuples if c[3]==active_year]
    currently_active_racer_ids = [v[0] for v in active_contracts]
    new_active_racer_tuples = []
    for racer_data in active_racer_tuples:
        r_id = racer_data[0]
        if r_id in currently_active_racer_ids: status = 'Aktif'
        else: status = 'Tidak Aktif'
        new_data = (r_id, racer_data[1], status)
        new_active_racer_tuples.append(new_data)
    active_racer_tuples = new_active_racer_tuples
    active_racers_dict = {id : (y, cs) for (id, y, cs) in active_racer_tuples}

    # -$ Penghargaan Generation
    award_count = gp_count * 3
    award_types = generate_bag(award_count, ['Fastest Lap', 'Driver of the Day', 'Most Positions Gained'], False)
    award_tuples = [(i+1, award_types[i]) for i in range(award_count)]

    # Diberi_Kepada Generation
    awarded_to_tuples = []
    for n, gp in enumerate(gp_tuples):
        gp_id = gp[0]
        
        valid_participants = [v[0] for v in participation_tuples if v[1]==gp_id]

        if not valid_participants:continue
        for i in range(1, 4):
            award_id = 3*n + i
            # get ids of racers in the gp
            receiver_id = rand.choice(valid_participants)
            awarded_to_tuples.append((receiver_id, gp_id, award_id))
        
    # convert all data to sql
    lines = []
    lines.extend([
        "DROP TABLE IF EXISTS Mengawasi;\n",
        "DROP TABLE IF EXISTS Diberi_kepada;\n",
        "DROP TABLE IF EXISTS Berpartisipasi_di;\n",
        "DROP TABLE IF EXISTS Memasok;\n",
        "DROP TABLE IF EXISTS Kontrak;\n",
        "DROP TABLE IF EXISTS Sesi;\n",
        "DROP TABLE IF EXISTS GrandPrix;\n",
        "DROP TABLE IF EXISTS Spesialisasi_Marshal;\n",
        "DROP TABLE IF EXISTS Pembalap_Pensiun;\n",
        "DROP TABLE IF EXISTS Pembalap_Aktif;\n",
        "DROP TABLE IF EXISTS Pembalap;\n",
        "DROP TABLE IF EXISTS Sirkuit;\n",
        "DROP TABLE IF EXISTS Tim;\n",
        "DROP TABLE IF EXISTS Marshal;\n",
        "DROP TABLE IF EXISTS Supplier_Mesin;\n",
        "DROP TABLE IF EXISTS Musim;\n",
        "DROP TABLE IF EXISTS Penghargaan;\n",
        "DROP TABLE IF EXISTS Negara;\n\n"
    ])

    lines.append("SET NAMES utf8mb4;\n\n")
    lines.extend(generate_create_tables())
    lines.append("SET autocommit=0;\n\n")
    lines.extend(convert_data_to_table('Negara', countries_tuples))
    lines.extend(convert_data_to_table('Tim', team_tuples))
    lines.extend(convert_data_to_table('Sirkuit', circuit_tuples))
    lines.extend(convert_data_to_table('Musim', season_tuples))
    lines.extend(convert_data_to_table('Penghargaan', award_tuples))
    lines.extend(convert_data_to_table('Supplier_Mesin', supplier_tuples))
    lines.extend(convert_data_to_table('Marshal', marshal_tuples))
    lines.extend(convert_data_to_table('Spesialisasi_Marshal', specialisation_tuples))
    lines.extend(convert_data_to_table('Pembalap', racer_tuples))
    lines.extend(convert_data_to_table('Pembalap_Aktif', active_racer_tuples))
    lines.extend(convert_data_to_table('Pembalap_Pensiun', retired_tuples))
    lines.extend(convert_data_to_table('GrandPrix', gp_tuples))
    lines.extend(convert_data_to_table('Sesi', session_tuples))
    lines.extend(convert_data_to_table('Kontrak', contract_tuples))
    lines.extend(convert_data_to_table('Memasok', supplies_tuples))
    lines.extend(convert_data_to_table('Berpartisipasi_di', participation_tuples))
    lines.extend(convert_data_to_table('Diberi_kepada', awarded_to_tuples))
    lines.extend(convert_data_to_table('Mengawasi', observes_tuples))
    lines.append("COMMIT;")

    with open(file_name, 'w', encoding='utf-8') as file:
        file.truncate(0); file.seek(0)
        for line in lines:
            file.write(line)
    
def sql_value(v):
    if isinstance(v, str):
        return "'" + v.replace("'", "''") + "'"
    return str(v)

def tuple_to_sql(t):
    vals = [sql_value(v) for v in t]
    return "(" + ", ".join(vals) + ")"

def generate_create_tables():
    return [
        """CREATE TABLE Negara (
    id_negara INT PRIMARY KEY,
    nama_negara VARCHAR(100)
);

""",

        """CREATE TABLE Penghargaan (
    id_penghargaan INT PRIMARY KEY,
    jenis_penghargaan VARCHAR(100)
);

""",

        """CREATE TABLE Musim (
    id_musim INT PRIMARY KEY,
    tahun INT,
    total_gp INT
);

""",

        """CREATE TABLE Supplier_Mesin (
    id_supplier INT PRIMARY KEY,
    nama_supplier VARCHAR(100)
);

""",

        """CREATE TABLE Marshal (
    id_marshal INT PRIMARY KEY,
    nama VARCHAR(100),
    level_sertifikasi VARCHAR(50)
);

""",

        """CREATE TABLE Tim (
    id_tim INT PRIMARY KEY,
    nama_tim VARCHAR(100),
    team_principal VARCHAR(100),
    anggaran_musim FLOAT,
    id_negara INT,
    FOREIGN KEY (id_negara) REFERENCES Negara(id_negara)
);

""",

        """CREATE TABLE Sirkuit (
    id_sirkuit INT PRIMARY KEY,
    nama_sirkuit VARCHAR(100),
    panjang_lintasan FLOAT,
    jumlah_tikungan INT,
    id_negara INT,
    FOREIGN KEY (id_negara) REFERENCES Negara(id_negara)
);

""",

        """CREATE TABLE Pembalap (
    id_pembalap INT PRIMARY KEY,
    nama VARCHAR(100),
    nomor_balap INT,
    total_poin INT,
    id_negara INT,
    FOREIGN KEY (id_negara) REFERENCES Negara(id_negara)
);

""",

        """CREATE TABLE Pembalap_Aktif (
    id_pembalap INT PRIMARY KEY,
    tahun_debut INT,
    status_kontrak VARCHAR(50),
    FOREIGN KEY (id_pembalap) REFERENCES Pembalap(id_pembalap)
);

""",

        """CREATE TABLE Pembalap_Pensiun (
    id_pembalap INT PRIMARY KEY,
    tahun_pensiun INT,
    total_balapan INT,
    FOREIGN KEY (id_pembalap) REFERENCES Pembalap(id_pembalap)
);

""",

        """CREATE TABLE Spesialisasi_Marshal (
    id_marshal INT,
    spesialisasi VARCHAR(100),
    PRIMARY KEY (id_marshal, spesialisasi),
    FOREIGN KEY (id_marshal) REFERENCES Marshal(id_marshal)
);

""",

        """CREATE TABLE GrandPrix (
    id_gp INT PRIMARY KEY,
    nama_gp VARCHAR(100),
    tanggal DATE,
    id_musim INT,
    id_sirkuit INT,
    FOREIGN KEY (id_musim) REFERENCES Musim(id_musim),
    FOREIGN KEY (id_sirkuit) REFERENCES Sirkuit(id_sirkuit)
);

""",

        """CREATE TABLE Sesi (
    id_sesi INT PRIMARY KEY,
    id_gp INT,
    jenis_sesi VARCHAR(50),
    tanggal DATE,
    FOREIGN KEY (id_gp) REFERENCES GrandPrix(id_gp)
);

""",

        """CREATE TABLE Kontrak (
    id_pembalap INT,
    id_tim INT,
    id_musim INT,
    musim_kontrak INT,
    PRIMARY KEY (id_pembalap, id_tim, id_musim),
    FOREIGN KEY (id_pembalap) REFERENCES Pembalap(id_pembalap),
    FOREIGN KEY (id_tim) REFERENCES Tim(id_tim),
    FOREIGN KEY (id_musim) REFERENCES Musim(id_musim)
);

""",

        """CREATE TABLE Memasok (
    id_supplier INT,
    id_tim INT,
    id_musim INT,
    PRIMARY KEY (id_supplier, id_tim, id_musim),
    FOREIGN KEY (id_supplier) REFERENCES Supplier_Mesin(id_supplier),
    FOREIGN KEY (id_tim) REFERENCES Tim(id_tim),
    FOREIGN KEY (id_musim) REFERENCES Musim(id_musim)
);

""",

        """CREATE TABLE Berpartisipasi_di (
    id_pembalap INT,
    id_gp INT,
    posisi_finish INT,
    waktu_tempuh VARCHAR(20),
    poin INT,
    PRIMARY KEY (id_pembalap, id_gp),
    FOREIGN KEY (id_pembalap) REFERENCES Pembalap(id_pembalap),
    FOREIGN KEY (id_gp) REFERENCES GrandPrix(id_gp)
);

""",

        """CREATE TABLE Diberi_kepada (
    id_pembalap INT,
    id_gp INT,
    id_penghargaan INT,
    PRIMARY KEY (id_pembalap, id_gp, id_penghargaan),
    FOREIGN KEY (id_pembalap) REFERENCES Pembalap(id_pembalap),
    FOREIGN KEY (id_gp) REFERENCES GrandPrix(id_gp),
    FOREIGN KEY (id_penghargaan) REFERENCES Penghargaan(id_penghargaan)
);

""",

        """CREATE TABLE Mengawasi (
    id_marshal INT,
    id_sesi INT,
    id_gp INT,
    PRIMARY KEY (id_marshal, id_sesi, id_gp),
    FOREIGN KEY (id_marshal) REFERENCES Marshal(id_marshal),
    FOREIGN KEY (id_sesi) REFERENCES Sesi(id_sesi),
    FOREIGN KEY (id_gp) REFERENCES GrandPrix(id_gp)
);

"""
    ]

def convert_data_to_table(table_name, data):
    lines = [f"INSERT INTO `{table_name}` VALUES\n",]

    for d in data:
        lines.append(f"{tuple_to_sql(d)},\n")

    if len(data) > 0:
        lines[-1] = f"{lines[-1][:-2]};\n"

    lines.append("\n")

    return lines

def generate_bag(n, values, do_shuffle=True):
    val = values[:]
    if do_shuffle: rand.shuffle(val)
    ret = []    
    while len(ret) < n:
        if val: ret.append(val.pop())
        else: 
            val = values[:] 
            if do_shuffle: rand.shuffle(val)
    return ret

if __name__ == '__main__': 
    main()
    