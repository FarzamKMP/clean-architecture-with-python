# ============================================================
# 🧩 Proxy Pattern
# Provides a surrogate or placeholder for another object to control access to it.
# یک شیء واسطه (Proxy) برای کنترل دسترسی به شیء واقعی (Real Object)
# گاهی نمی‌خوای یا نمی‌تونی مستقیماً با یک شیء اصلی کار کنی.
# مثلاً ممکنه:
# ساخت یا دسترسی به اون شیء گرون باشه (مثل اتصال دیتابیس)،
# یا بخوای قبل از دسترسی، کنترل دسترسی یا کش انجام بدی.
# در این حالت، یه کلاس Proxy می‌سازی که رفتار اصلی رو کنترل یا محدود می‌کنه.
# ============================================================

from time import sleep

# The real object that does the heavy work
class YouTubeVideo:
    def __init__(self, video_id):
        self.video_id = video_id
        self._load_from_server()

    def _load_from_server(self):
        print(f"Loading video {self.video_id} from YouTube server...")
        sleep(1)  # simulate heavy network loading
        print("Video loaded successfully.")

    def play(self):
        print(f"Playing video {self.video_id}...")


# The Proxy object
class YouTubeProxy:
    def __init__(self):
        self._cache = {}  # cache loaded videos

    def play_video(self, video_id):
        # Check if video already loaded (cached)
        if video_id not in self._cache:
            print(f"[Proxy] Video not in cache, loading...")
            self._cache[video_id] = YouTubeVideo(video_id)
        else:
            print(f"[Proxy] Playing cached video...")
        self._cache[video_id].play()


# Usage Example
proxy = YouTubeProxy()
proxy.play_video("abc123")  # Loads from server
print("---")
proxy.play_video("abc123")  # Plays from cache
print("---")
proxy.play_video("xyz789")  # Loads a new video


#در دنیای واقعی، چند نوع Proxy داریم:
# Type	Description	Example
# Virtual Proxy	بارگذاری تنبل (Lazy Loading) برای اشیاء سنگین	بارگذاری فایل یا ویدیو فقط در زمان نیاز
# Remote Proxy	کنترل دسترسی به اشیاء در سرورهای دور	gRPC، API Gateway
# Protection Proxy	بررسی سطح دسترسی کاربران قبل از اجرا	Authorization system
# Caching Proxy	ذخیره نتیجه برای افزایش کارایی	YouTube / Web cache