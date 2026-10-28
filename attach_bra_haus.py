import json
from domainconnectzone import process_records

def attach_github_domain(domain: str, github_username: str, zone_records: list = None):
    if zone_records is None:
        zone_records = []

    template_records = [
        {"type": "A", "host": "@", "pointsTo": "185.199.108.153", "ttl": 3600},
        {"type": "A", "host": "@", "pointsTo": "185.199.109.153", "ttl": 3600},
        {"type": "A", "host": "@", "pointsTo": "185.199.110.153", "ttl": 3600},
        {"type": "A", "host": "@", "pointsTo": "185.199.111.153", "ttl": 3600},
        {"type": "CNAME", "host": "www", "pointsTo": "%GH_USERNAME%.github.io", "ttl": 3600}
    ]

    params = {
        "GH_USERNAME": github_username
    }

    new_records, deleted_records, final_records = process_records(
        template_records=template_records,
        zone_records=zone_records,
        domain=domain,
        host="",
        params=params,
        group_ids=[]
    )

    return {
        "new_records": new_records,
        "deleted_records": deleted_records,
        "final_records": final_records
    }


if __name__ == "__main__":
    import sys
    username = sys.argv[1] if len(sys.argv) > 1 else "your-github-username"
    domain = "bra.haus"

    result = attach_github_domain(domain=domain, github_username=username)

    print(f"=== Результат формирования DNS-записей для {domain} (GitHub Pages: {username}.github.io) ===")
    print("\n[Новые/Обновленные записи]:")
    print(json.dumps(result["new_records"], indent=2))
    print("\n[Удаляемые старые записи]:")
    print(json.dumps(result["deleted_records"], indent=2))
    print("\n[Итоговые записи зоны]:")
    print(json.dumps(result["final_records"], indent=2))
