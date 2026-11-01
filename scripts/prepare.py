import math,struct,wave,os,re
d='android/app/src/main/res/raw'; os.makedirs(d,exist_ok=True)
sr=22050; w=wave.open(d+'/alarm.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
fr=[]
for i in range(sr*20):
    t=i/sr; on=(t%0.8)<0.4
    fr.append(struct.pack('<h',int(24000*math.sin(2*math.pi*880*t)*(1-(t%0.8)/0.4))) if on else struct.pack('<h',0))
w.writeframes(b''.join(fr)); w.close()
p='android/app/src/main/AndroidManifest.xml'; s=open(p,encoding='utf-8').read()
perms='<uses-permission android:name="android.permission.USE_EXACT_ALARM"/><uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM"/><uses-permission android:name="android.permission.POST_NOTIFICATIONS"/><uses-permission android:name="android.permission.VIBRATE"/>'
s=s.replace('</manifest>',perms+'</manifest>'); open(p,'w',encoding='utf-8').write(s)
