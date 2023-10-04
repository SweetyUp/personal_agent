from data_tools import *

def haruhi2GLM(init_path,save_path):
    init_path = r'/Users/xiaotianqi/code/GraduationPrj/dataset/init_dataset/Haruhi_54K_v1.jsonl'
    init_data = jsonl2dict(init_path)
    len(init_data)

    for i in init_data:
        agent_name = i['agent_role']
        user_name = i['user_role']
        user_dial = i['user_question']
        agent_dial = i['agent_response']
        language_prompt = ''
        
        # 清除掉所有旁白 
        if i['user_role'] == '旁白' or i['user_role'] == 'scene':
            continue
        user_dial_language = detect_language(user_dial)
        agent_dial_language = detect_language(agent_dial)
        # 处理中英混杂的数据 
        if user_dial_language == '英文' and agent_dial_language == '中文':
            language_prompt = 'speak chinese.'
        if user_dial_language == '中文' and agent_dial_language == '英文':
            language_prompt = '请讲英语。'
        prompt = f'''你现在需要沉浸式扮演{agent_name}，请你按照{agent_name}的语言风格，性格特点与{user_name}对话。{language_prompt}现在{user_name}对你说{user_dial}作为{agent_name}，你将会回复：'''
        temp_save_data = {"prompt":prompt,"response":agent_dial}
        data2jsonl(save_path,temp_save_data)

def main():
    init_path = r'/Users/xiaotianqi/code/GraduationPrj/dataset/init_dataset/Haruhi_54K_v1.jsonl'
    save_path = r'/Users/xiaotianqi/code/GraduationPrj/dataset/pro_dataset/Haruhi_50K_v1.jsonl'
    haruhi2GLM(init_path,save_path)


if __name__ == "__main__":
    main()