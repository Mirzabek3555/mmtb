from django.core.management.base import BaseCommand
from main.models import SiteSettings, Statistics, Announcement
from news.models import News, NewsCategory
from schools.models import School
from staff_app.models import Staff, Department
from gallery.models import GalleryCategory


class Command(BaseCommand):
    help = "Demo ma'lumotlar yaratish"

    def handle(self, *args, **kwargs):
        # 1. Site Settings
        if not SiteSettings.objects.exists():
            SiteSettings.objects.create(
                organization_name="Tuproqqal'a Tuman MTB",
                organization_full_name="Tuproqqal'a Tuman Maktabgacha va Maktab Ta'limi Bo'limi",
                address="Qashqadaryo viloyati, Tuproqqal'a tumani, Markaziy ko'cha 12",
                phone="+998 65 222-00-00",
                phone2="+998 65 222-00-01",
                email="info@tuproqqala-talim.uz",
                working_hours="Dushanba-Juma: 9:00 - 18:00",
                telegram="https://t.me/tuproqqala_talim",
                about_text="Tuproqqal'a tuman maktabgacha va maktab ta'limi bo'limi Qashqadaryo viloyati Tuproqqal'a tumanida ta'lim sohasini boshqarish uchun mas'ul tashkilotdir. Biz tuman bo'yicha barcha ta'lim muassasalarining faoliyatini muvofiqlashtirgan holda, bolalar va yoshlarning sifatli ta'lim olishini ta'minlaymiz.",
            )
            self.stdout.write("✓ Sayt sozlamalari yaratildi")

        # 2. Statistics
        if not Statistics.objects.exists():
            stats = [
                ("Ta'lim muassasalari", "42", "fas fa-school", 1),
                ("O'quvchi va tarbiyalanuvchilar", "14200", "fas fa-user-graduate", 2),
                ("Pedagoglar", "920", "fas fa-chalkboard-teacher", 3),
                ("MTM muassasalari", "28", "fas fa-baby", 4),
            ]
            for title, value, icon, order in stats:
                Statistics.objects.create(title=title, value=value, icon=icon, order=order)
            self.stdout.write("✓ Statistikalar yaratildi")

        # 3. Announcements
        if not Announcement.objects.exists():
            Announcement.objects.create(
                title="2024-2025 o'quv yili qabul hujjatlari ro'yxatga olish boshlandi",
                content="Barcha maktabgacha ta'lim muassasalariga qabul hujjatlarini topshirish mumkin.",
            )
            Announcement.objects.create(
                title="Pedagoglar uchun malaka oshirish kurslari ro'yxati e'lon qilindi",
                content="Sentyabr oyida malaka oshirish kurslari boshlanadi.",
            )
            self.stdout.write("✓ E'lonlar yaratildi")

        # 4. News Categories
        cat1, _ = NewsCategory.objects.get_or_create(name="Yangiliklar", slug="yangiliklar")
        cat2, _ = NewsCategory.objects.get_or_create(name="Tadbirlar", slug="tadbirlar")
        cat3, _ = NewsCategory.objects.get_or_create(name="E'lonlar", slug="elonlar")

        # 5. News
        if not News.objects.exists():
            news_items = [
                ("2024-2025 o'quv yili boshlandi", "Tuman bo'yicha barcha maktab va maktabgacha ta'lim muassasalarida yangi o'quv yili tantanali tarzda boshlandi.", cat1, True),
                ("Yangi maktab binosi qurilishi yakunlandi", "Tuproqqal'a tumanida zamonaviy jihozlangan yangi maktab binosi qurilishi muvaffaqiyatli yakunlandi.", cat1, True),
                ("Respublika olimpiadasida g'olib", "Tuman maktablaridan o'quvchilar respublika olimpiadasida yuqori o'rinlarni egalladi.", cat2, True),
                ("Pedagoglar malaka oshirish kurslari", "Sentyabr oyida tuman pedagoglari uchun malaka oshirish kurslari bo'lib o'tdi.", cat2, False),
                ("Maktabgacha ta'lim muassasasiga qabul", "Yangi o'quv yilida maktabgacha ta'lim muassasasiga qabul ro'yxatga olish davom etmoqda.", cat3, False),
            ]
            for title, desc, cat, featured in news_items:
                News.objects.create(
                    title=title,
                    short_description=desc,
                    content=f"<p>{desc}</p><p>Batafsil ma'lumot uchun bo'limimizga murojaat qilishingiz mumkin.</p>",
                    category=cat,
                    is_featured=featured,
                    is_published=True,
                )
            self.stdout.write("✓ Yangiliklar yaratildi")

        # 6. Schools
        if not School.objects.exists():
            schools = [
                ("1-son umumta'lim maktabi", "maktab", "1", "Markaziy ko'cha 1", "+998 65 222-01-00", "Karimov Xurshid Baxtiyorovich", 450, 32),
                ("2-son umumta'lim maktabi", "maktab", "2", "Bog'ishamol ko'chasi 5", "+998 65 222-02-00", "Toshmatova Dilnoza Umarovna", 380, 28),
                ("3-son umumta'lim maktabi", "maktab", "3", "Navruz ko'chasi 10", "+998 65 222-03-00", "Rahimov Baxtiyor Siddiqovich", 520, 35),
                ("Gulbahor maktabgacha ta'lim muassasasi", "maktabgacha", "", "Markaziy ko'cha 3", "+998 65 222-04-00", "Yusupova Nodira Hamidovna", 180, 14),
                ("Bahor maktabgacha ta'lim muassasasi", "maktabgacha", "", "Park ko'chasi 8", "+998 65 222-05-00", "Mirzayeva Maftuna Aliyevna", 150, 12),
            ]
            for name, stype, num, addr, phone, director, students, teachers in schools:
                School.objects.create(
                    name=name, school_type=stype, number=num, address=addr,
                    phone=phone, director_name=director,
                    student_count=students, teacher_count=teachers, founded_year=1990,
                    description=f"<p>{name} tuman bo'yicha yetakchi ta'lim muassasalaridan biri hisoblanadi.</p>"
                )
            self.stdout.write("✓ Maktablar yaratildi")

        # 7. Departments and Staff
        if not Department.objects.exists():
            dept1 = Department.objects.create(name="Maktab ta'limi bo'limi", order=1)
            dept2 = Department.objects.create(name="Maktabgacha ta'lim bo'limi", order=2)
            dept3 = Department.objects.create(name="Moliya-xo'jalik bo'limi", order=3)

            Staff.objects.create(
                full_name="Abdullayev Jasur Rauf o'g'li",
                position="rahbar",
                position_custom="Bo'lim boshlig'i",
                phone="+998 65 222-00-10",
                reception_hours="Dushanba-Juma: 14:00 - 17:00",
                is_management=True, order=1
            )
            Staff.objects.create(
                full_name="Xoliqova Zilola Hamidovna",
                position="rahbar",
                position_custom="Bo'lim boshlig'i o'rinbosari",
                phone="+998 65 222-00-11",
                reception_hours="Seshanba-Payshanba: 10:00 - 12:00",
                is_management=True, order=2
            )
            Staff.objects.create(
                full_name="Qodirov Mansur Erkinovich",
                position="bosh_mutaxassis",
                department=dept1, phone="+998 65 222-00-12", order=3
            )
            Staff.objects.create(
                full_name="Tursunova Muazzam Salimovna",
                position="mutaxassis",
                department=dept2, phone="+998 65 222-00-13", order=4
            )
            Staff.objects.create(
                full_name="Choriyev Dilshod Nazarovich",
                position="mutaxassis",
                department=dept3, phone="+998 65 222-00-14", order=5
            )
            self.stdout.write("✓ Xodimlar yaratildi")

        # 8. Gallery Category
        if not GalleryCategory.objects.exists():
            GalleryCategory.objects.create(name="Tadbirlar")
            GalleryCategory.objects.create(name="Maktablar")
            GalleryCategory.objects.create(name="O'quv jarayoni")
            self.stdout.write("✓ Galereya kategoriyalari yaratildi")

        self.stdout.write(self.style.SUCCESS("\n🎉 Barcha demo ma'lumotlar muvaffaqiyatli yaratildi!"))
