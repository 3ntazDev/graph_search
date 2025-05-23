# مشروع خوارزميات البحث في الرسوم البيانية 🧑‍💻

## 🚀 مقدمة
هذا المشروع يهدف إلى تطبيق بعض خوارزميات البحث الشهيرة في الرسوم البيانية باستخدام مكتبة `Tkinter` لإنشاء واجهة المستخدم الرسومية. يتم تنفيذ خوارزميات مثل:
- **BFS (بحث بالعرض)**.
- **DFS (بحث بالعمق)**.
- **A\* (بحث مسار باستخدام خوارزمية A\*)**.
  
تدير الواجهة الرسومية العقد والروابط وتسمح للمستخدم بإضافة عقد جديدة، إنشاء روابط بين العقد، وتنفيذ الخوارزميات المختلفة.

## 🛠 المتطلبات
لتشغيل هذا المشروع، يجب أن تكون لديك البيئة التالية:
1. **Python** (يفضل الإصدار 3.6 أو أعلى).
2. **Tkinter** (مضمن مع Python بشكل افتراضي).
3. **مكتبة `random` و `heapq` و `collections`** (مكتبات مدمجة في Python).

## 📦 كيفية تشغيل البرنامج
1. **تحميل المشروع**:
   - قم بتحميل الكود المصدري إلى جهازك.

2. **تشغيل البرنامج**:
   - افتح المحرر المفضل لديك أو **Terminal**.
   - انتقل إلى مجلد المشروع.
   - قم بتشغيل البرنامج عبر الأمر:
     ```bash
     python3 main.py
     ```

   سيفتح البرنامج نافذة واجهة المستخدم الرسومية التي يمكنك من خلالها إضافة العقد، إنشاء الروابط، واختيار الخوارزميات.

## 🎮 الواجهة الرسومية
- **إضافة عقدة**: إضافة عقدة جديدة إلى الرسم البياني في مكان عشوائي.
- **إضافة رابط**: إنشاء رابط بين عقدتين عشوائيتين.
- **BFS / DFS / A\***: تنفيذ الخوارزميات وعرض المسار بين العقد.
- **مسح**: مسح جميع العقد والروابط وإعادة تعيين الرسم البياني.
- **دمج العقد**: دمج العقد باستخدام خوارزمية `Union-Find` لتحديد المجموعات المتصلة.

## 📝 التفاصيل التقنية
- **Canvas**: يتم استخدام `tk.Canvas` لعرض العقد والروابط.
- **أحداث الماوس**:
  - **ضغط الماوس**: لتحديد العقدتين بداية ونهاية الخوارزمية.
  - **تحريك الماوس**: لتحريك العقد داخل الواجهة.
  
- **خوارزميات البحث**:
  - **BFS (بحث بالعرض)**: يستخدم قائمة انتظار (`queue`) لاستكشاف جميع العقد على مستوى واحد قبل الانتقال إلى المستوى التالي.
  - **DFS (بحث بالعمق)**: يستخدم مكدس (`stack`) لاستكشاف العقد حتى الوصول إلى هدف قبل العودة.
  - **A\* (بحث مسار)**: يستخدم خوارزمية البحث المسار الأمثل باستخدام `heapq` مع تقدير المسافة الإقليدية بين العقد.

- **Union-Find**: لتحديد المجموعات المتصلة في الرسم البياني، مما يساعد في إدارة العقد المرتبطة.

## 🎨 التخصيص والميزات
- **تصميم واجهة المستخدم**:
  - الواجهة تم تصميمها باستخدام مكتبة `Tkinter`.
  - يمكن للمستخدم إضافة عقدة جديدة وتحريك العقد في مساحة العمل.
  
- **التمثيل البصري**:
  - يتم رسم العقد كدوائر ملونة تمثل العقد.
  - يتم رسم الروابط بين العقد كخطوط بين العقدتين.
  - المسار الناتج من الخوارزميات يتم تمييزه بلون أحمر.

## ❓ ملاحظات
- تأكد من تحديد عقدة البداية والنهاية قبل تنفيذ الخوارزميات.
- إذا كانت الرسالة "لا يوجد مسار" تظهر، فهذا يعني أنه لا يمكن الوصول إلى العقدة الهدف باستخدام الخوارزمية المختارة.
  


🔑 تمتع بتجربة استخدام الخوارزميات واستكشاف الرسوم البيانية!
