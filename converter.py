import json

csv = open('optd_por_public.csv', 'r').read().split('\n')

firstLine = True

gj = {
  "type": "FeatureCollection",
  "features": [ ]
}

for line in csv:
    if (firstLine):
        firstLine = False
        continue
    line = line.split('^')
    if len(line) < 10:
        continue
    try:
        lat = float(line[8])
        lng = float(line[9])
    except:
        print('failed to parse location for: ' + line[6])
        continue
    gj["features"].append({
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [lng, lat]
          },
          "properties": {
            "iata_code": line[0],
            "icao_code": line[1],
            "faa_code": line[2],
            "is_geonames": line[3],
            "geoname_id": line[4],
            "envelope_id": line[5],
            "name": line[6],
            "asciiname": line[7],
            "fclass": line[10],
            "fcode": line[11],
            "page_rank": line[12],
            "date_from": line[13],
            "date_until": line[14],
            "comment": line[15],
            "country_code": line[16],
            "cc2": line[17],
            "country_name": line[18],
            "continent_name": line[19],
            "adm1_code": line[20],
            "adm1_name_utf": line[21],
            "adm1_name_ascii": line[22],
            "adm2_code": line[23],
            "adm2_name_utf": line[24],
            "adm2_name_ascii": line[25],
            "adm3_code": line[26],
            "adm4_code": line[27],
            "population": line[28],
            "elevation": line[29],
            "gtopo30": line[30],
            "timezone": line[31],
            "gmt_offset": line[32],
            "dst_offset": line[33],
            "raw_offset": line[34],
            "moddate": line[35],
            "city_code_list": line[36],
            "city_name_list": line[37],
            "city_detail_list": line[38],
            "tvl_por_list": line[39],
            "state_code": line[40],
            "location_type": line[41],
            "wiki_link": line[42],
            "alt_name_section": line[43],
            "wac": line[44],
            "wac_name": line[45]
        }
    })

gjout = open('optd_por_public.geojson', 'w')
gjout.write(json.dumps(gj))
