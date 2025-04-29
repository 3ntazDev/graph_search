import tkinter as tk  # عشان استخدام مكتبة tkinter لإنشاء واجهة المستخدم الرسومية
from tkinter import messagebox  # عشان اعرض رسائل الخطأ
from collections import deque  # عشان استخدام deque في خوارزمية BFS
import heapq  # عشان استخدام heapq في خوارزمية A* توجد لي min Heap
import random  # عشان استخدام random لإضافة العقد والروابط بشكل عشوائي

class GraphApp:
    def __init__(self, root):  # دالة الكونستركتر هنا
        self.root = root
        self.root.title("خوارزميات البحث في الرسوم البيانية")
        self.root.geometry("700x500")

        # تقدر تقول المتغيرات اللي راح نغزن فيها للرسم
        self.nodes = {}
        self.edges = []
        self.start = None
        self.goal = None
        
        # لتخزين الـ Union-Find
        self.parent = {}
        self.rank = {}

        # إنشاء الواجهة
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # شريط الأدوات
        toolbar = tk.Frame(root)
        toolbar.pack(fill=tk.X)

        # هنا الازارات اللي راح نستخدمها
        buttons = [
            ("إضافة عقدة", self.add_node),
            ("إضافة رابط", self.add_edge),
            ("BFS", lambda: self.search("BFS")),
            ("DFS", lambda: self.search("DFS")),
            ("A*", lambda: self.search("A*")),
            ("مسح", self.clear),
            ("دمج العقد", self.union_find)  # زر الدمج
        ]

        for text, command in buttons:
            tk.Button(toolbar, text=text, command=command).pack(side=tk.LEFT)

        # ربط أحداث الماوس
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
     
    def add_node(self):
        # إضافة عقدة في موقع عشوائي
        node_id = f"N{len(self.nodes)+1}"
        self.nodes[node_id] = (random.randint(50, 650), random.randint(50, 450))
        self.draw()
    
    def add_edge(self):
        # إضافة رابط بين أول عقدتين
        if len(self.nodes) < 2:
            messagebox.showerror("خطأ", "يجب إضافة عقدتين على الأقل")
            return
        
        nodes = list(self.nodes.keys())
        n1, n2 = random.sample(nodes, 2)  # اختيار عقدتين عشوائيتين
        weight = random.randint(1, 10)
        self.edges.append((n1, n2, weight))
        self.draw()
    
    def on_click(self, event):
        # تحديد عقدة البداية أو النهاية
        node = self.find_node_at(event.x, event.y)
        if node:
            if not self.start:
                self.start = node
            elif not self.goal and node != self.start:
                self.goal = node
            self.draw()
    
    def on_drag(self, event):
        # تحريك العقدة
        node = self.find_node_at(event.x, event.y)
        if node:
            self.nodes[node] = (event.x, event.y)
            self.draw()
    
    def find_node_at(self, x, y):
        # البحث عن عقدة في الموقع المحدد
        for node, (nx, ny) in self.nodes.items():
            if ((nx - x)**2 + (ny - y)**2) <= 400:  # نصف قطر 20
                return node
        return None
    
    def search(self, algorithm):
        # التحقق من وجود عقدة بداية ونهاية
        if not self.start or not self.goal:
            messagebox.showerror("خطأ", "يرجى تحديد عقدة البداية والنهاية")
            return
        
        # تنفيذ الخوارزمية المناسبة
        path = []
        if algorithm == "BFS":
            path = self.bfs()
        elif algorithm == "DFS":
            path = self.dfs()
        elif algorithm == "A*":
            path = self.a_star()
        
        # عرض النتيجة
        self.draw(path)
        result = "المسار: " + " → ".join(path) if path else "لا يوجد مسار"
        messagebox.showinfo("نتيجة البحث", result)
    
    def get_neighbors(self, node):
        # الحصول على العقد المجاورة
        neighbors = []
        for a, b, weight in self.edges:
            if a == node:
                neighbors.append((b, weight))
            elif b == node:
                neighbors.append((a, weight))
        return neighbors
    
    def bfs(self):
        # خوارزمية البحث بالعرض
        queue = deque([(self.start, [self.start])])
        visited = {self.start}
        
        while queue:
            node, path = queue.popleft()
            if node == self.goal:
                return path
            
            for neighbor, _ in self.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return []
    
    def dfs(self):
        # خوارزمية البحث بالعمق
        stack = [(self.start, [self.start])]
        visited = {self.start}
        
        while stack:
            node, path = stack.pop()
            if node == self.goal:
                return path
            
            for neighbor, _ in self.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))
        
        return []
    
    def a_star(self):
        # خوارزمية A*
        def heuristic(node):
            # المسافة الإقليدية
            x1, y1 = self.nodes[node]
            x2, y2 = self.nodes[self.goal]
            return ((x1-x2)**2 + (y1-y2)**2)**0.5
        
        open_set = [(heuristic(self.start), 0, self.start, [self.start])]
        closed_set = set()
        
        while open_set:
            _, cost, node, path = heapq.heappop(open_set)
            
            if node == self.goal:
                return path
                
            if node in closed_set:
                continue
                
            closed_set.add(node)
            
            for neighbor, weight in self.get_neighbors(node):
                if neighbor not in closed_set:
                    new_cost = cost + weight
                    heapq.heappush(open_set, (
                        new_cost + heuristic(neighbor),
                        new_cost,
                        neighbor,
                        path + [neighbor]
                    ))
        
        return []
    
    def draw(self, path=None):
        # رسم الرسم البياني
        self.canvas.delete("all")
        
        # رسم الروابط
        for a, b, weight in self.edges:
            x1, y1 = self.nodes[a]
            x2, y2 = self.nodes[b]
            self.canvas.create_line(x1, y1, x2, y2, width=2)
            self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=str(weight))
        
        # رسم المسار إذا وجد
        if path and len(path) > 1:
            for i in range(len(path)-1):
                a, b = path[i], path[i+1]
                x1, y1 = self.nodes[a]
                x2, y2 = self.nodes[b]
                self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3)
        
        # رسم العقد
        for node, (x, y) in self.nodes.items():
            color = "lightblue"
            if node == self.start:
                color = "green"
            elif node == self.goal:
                color = "red"
            elif path and node in path:
                color = "orange"
            
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color)
            self.canvas.create_text(x, y, text=node)
    
    def clear(self):
        # إعادة تعيين الرسم البياني
        self.nodes = {}
        self.edges = []
        self.start = None
        self.goal = None
        self.canvas.delete("all")

    def union_find(self):
        # خوارزمية Union-Find
        def find(x):
            # البحث في الـ parent لإيجاد الجذر
            if self.parent[x] != x:
                self.parent[x] = find(self.parent[x])  # الـ Path compression
            return self.parent[x]

        def union(x, y):
            # دمج المجموعات باستخدام الـ Rank
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1
        
        # هنا نبدأ في تهيئة الـ parent والـ rank لكل عقدة
        for node in self.nodes:
            self.parent[node] = node
            self.rank[node] = 0
        
        # نفترض أن كل رابط بين عقدتين نقوم بدمجهما
        for a, b, _ in self.edges:
            union(a, b)
        
        messagebox.showinfo("Union-Find", "تم دمج المجموعات بنجاح!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
