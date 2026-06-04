import vk_api


vk_session = vk_api.VkApi(token='vk1.a.lXTBMuY4ii9qi2simLs7phI__FhN1sexNnMU8L5KfvVnljt8ZsFn0MkyHD2n-CHoNhJR9L6AfB7q68n-RlO_CeKZVySshLwbiqrMpD1sogtXmAE3qRmfLJWf6kgQvRydgHUGLL5hy4_sU0_KABjUrg5dQhOIIZ2hysBnudhmJfLVIsr3wnD5ohWr5u3_bHGY4HOKEmLqHjJcdj62z_nYYA',)
vk = vk_session.get_api()


# CONFIG ===>
club_name = "club229112291"

# <==========


vk.messages.send(domain=club_name, random_id="int32", message="ВОЫОЛВФОЛД")
