import http.client
import json
import time
token = "YOUR TOKEN DISCORD"
# อ่าน config.json
with open(r'../config.json') as f:
    config_data = json.load(f)
    channel_configs = config_data['Config']  # รายการช่อง
    

header_data = { 
    "Content-Type": "application/json", 
    "User-Agent": "DiscordBot", 
    "Authorization": token  
} 

def get_connection(): 
    return http.client.HTTPSConnection("discord.com", 443) 

def send_message(conn, channel_id, message_data): 
    print(message_data) 
    try: 
        conn.request("POST", f"/api/v10/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print(f"Message sent to channel {channel_id}.")
        else: 
            print(f"HTTP {resp.status}: {resp.reason} for channel {channel_id}")
    except Exception as e: 
        print(f"Error sending message to channel {channel_id}: {e}") 

def main(): 
    for channel in channel_configs:
        channel_id = channel['channelid']
        message = channel['message']
        message_data = { 
            "content": message, 
            "tts": False
        }
        time.sleep(1)
        
        send_message(get_connection(), channel_id, json.dumps(message_data)) 

if __name__ == '__main__': 
    while True:    
        main()      
        time.sleep(7200)  # หน่วงเวลา 2 ชั่วโมง
