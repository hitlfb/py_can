import sqlite3
import os
from datetime import datetime

# 数据库配置
DB_NAME = 'can_data.db'
TABLE_NAME = 'can_messages'

def init_database():
    """初始化数据库和表结构"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 创建表（如果不存在）
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME NOT NULL,
            can_id INTEGER NOT NULL,
            dlc INTEGER NOT NULL,
            data BLOB NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def save_can_data(can_id, dlc, data):
    """保存CAN数据到数据库"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 插入数据
    cursor.execute(f'''
        INSERT INTO {TABLE_NAME} (timestamp, can_id, dlc, data)
        VALUES (?, ?, ?, ?)
    ''', (datetime.now(), can_id, dlc, data))
    
    conn.commit()
    conn.close()

"""
# 初始化数据库
init_database()

# 示例：模拟接收CAN数据并保存
# 实际使用时需替换为真实的CAN数据获取代码（如使用python-can库）
sample_can_data = [
    (0x123, 8, b'\x01\x02\x03\x04\x05\x06\x07\x08'),
    (0x456, 4, b'\xAA\xBB\xCC\xDD'),
]

for can_id, dlc, data in sample_can_data:
    save_can_data(can_id, dlc, data)
    print(f"已保存CAN数据: ID={hex(can_id)}, DLC={dlc}, Data={data.hex()}")"""