import os 
import time 
import random 
import datetime 
from colorama import init, Fore, Style 
from fpdf import FPDF

Terminal renklerini başlat

init(autoreset=True)

Platform listesi

platforms = ["Facebook", "Google", "Instagram", "Twitter", "LinkedIn", "TikTok"] 
responses = ["Silme talebi alındı.", "İşleme alındı.", "Veri silindi.", "Kullanıcı hesabı bulunamadı.", "Hukuki değerlendirmeye alındı."]

SilBot karakteri

class SilBot:
  def speak(self, message, delay=0.03):
    for char in message:
      print(Fore.CYAN + char, end="", flush=True) time.sleep(delay)
    print(Style.RESET_ALL)

def action(self, status):
    colors = [Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.MAGENTA]
    print(random.choice(colors) + f"➡️  {status}" + Style.RESET_ALL)

silbot = SilBot()

def yükle_targets(dosya="targets.txt"):
  if not os.path.exists(dosya):
    silbot.speak("targets.txt bulunamadı. Örnek veriler ekleniyor...")
    with open(dosya, "w") as f:
      f.write("ahmet@example.com\n+905331112233\nmyusername")
  with open(dosya, "r") as f:
    return [line.strip() for line in f if line.strip() != ""]

def animasyon():
  for _ in range(3):
    print(Fore.YELLOW + "." * random.randint(3, 10), end=" ", flush=True) time.sleep(0.4)
  print()

def pdf_uret(veri_listesi):
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Arial", size=12)
  pdf.cell(200, 10, txt="Silme Başvuru Raporu", ln=True, align="C") pdf.cell(200, 10, txt=str(datetime.datetime.now()), ln=True, align="C") 
  pdf.ln(10)
  for veri in veri_listesi:
    pdf.cell(200, 10, txt=f"Veri: {veri}", ln=True)
    if not os.path.exists("belge"):
      os.makedirs("belge")
      pdf.output("belge/silme_raporu.pdf")
      silbot.speak("📄 PDF raporu oluşturuldu. (belge/silme_raporu.pdf)")

def log_yaz(veri, sonuc):
  zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("log.txt", "a") as f:
    f.write(f"[{zaman}] {veri} -> {sonuc}\n")

if name == "main":
  silbot.speak("\n🔐 SilBeni Simülasyonuna Hoş Geldin.")
  silbot.speak("Dijital geçmişini silmek artık çok daha bilinçli bir eylem.")

veriler = yükle_targets()
silbot.speak(f"{len(veriler)} veri bulundu. İşlem başlatılıyor...\n")
time.sleep(1)

for veri in veriler:
    platform = random.choice(platforms)
    durum = random.choice(responses)
    silbot.speak(f"\n🗂️ Veri: {veri} — Platform: {platform}")
    animasyon()
    silbot.action(durum)
    log_yaz(veri, durum)

pdf_uret(veriler)
silbot.speak("\n✅ Simülasyon tamamlandı. Log ve belge dosyalarınız hazır.")

