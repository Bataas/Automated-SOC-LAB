import json

cases = json.loads(r'''$iris_search_case''')["body"]["data"]["cases"]

dedup_tag = json.loads(
    r'''$build_soc_context'''
)["message"]["dedup_tag"]

matched_case = None

for case in cases:

    if dedup_tag in str(case):

        matched_case = case
        break

result = {
    "found": matched_case is not None,
    "case_id": matched_case["case_id"] if matched_case else None,
    "case_uuid": matched_case["case_uuid"] if matched_case else None,
    "case_name": matched_case["name"] if matched_case else None
}

print(json.dumps(result))