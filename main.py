from utils.zoneTelechargementLinkExtractor import ZoneTelechargementLinkExtractor

if __name__ == '__main__':
    ZoneTelechargementLinkExtractor().find_multi_links([
        "https://www.zone-telechargement.pics/?p=serie&id=4511-good-doctor-saison3",
        "https://www.zone-telechargement.pics/?p=serie&id=12286-good-doctor-saison4",
        "https://www.zone-telechargement.pics/?p=serie&id=15560-good-doctor-saison5",
        "https://www.zone-telechargement.pics/?p=serie&id=16099-good-doctor-saison6"
    ])
