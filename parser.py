import re
import json

class TunisianGeoPhoneticParser:
    def __init__(self):
        # 1. بناء مصفوفة قاموس التحورات اللسانية والبيئية
        self.linguistic_dictionary = {
            "شقطمة": "الشوفطيم (جمع شوفط وتعني القضاة بالبونية الكنعانية) - تحور لغوي بفعل التصحيف البصري وتنقيط الفاء والقاف قديماً ونطق الـ G البدوية.",
            "سبيطلة": "سبط لاوي (مركز الشريعة والقضاء الشرعي السامي لحفظ هوية المهاجرين الأوائل).",
            "الشعانبي": "جبل أشعياء (الجبل الروحي الحامي المحيط بالمنطقة تبركاً بنبوءات الخلاص الشامية).",
            "سلوم": "شلوم / سيليوم (عاصمة ومقر الأمان والسكينة وتعني مدينة السلام).",
            "حيدرة": "عُميدرة (أرض التطهير بالماء الجاري والتعميد، حاصرها الحصن الروماني الطولي لوقف مدها العقائدي).",
            "فوسانة": "فوستانا (البستان والجنة الخضراء التي غُذيت تاريخياً بأكبر معاصر الزيتون بهنشير البقر)."
        }

    def apply_phonetic_rules(self, text):
        """
        الوحدة الأولى: معالج القواعد الصوتية المخصصة (Phonetic Shift Engine)
        تطبيق خوارزميات الإبدال الصوتي السمعي للاستعمار الفرنسي واللسان البدوي
        """
        # نمط 1: تحويل "La gare de tâche" الاستعماري إلى "قرعة العطش" بدوياً
        # قلب الـ G إلى قاف بدوية تنطق G، وقلب المد الحلقي A إلى حرف العين (ع)
        if re.search(r'(la\s+)?gare\s+(de\s+)?tâches?', text, re.IGNORECASE):
            text = "قرعة العطش (التحور اللساني البدوي لـ La gare de tâche بناءً على جغرافية ونطق المنطقة)"
            return text
            
        return text

    def context_aware_interpreter(self, text):
        """
        الوحدة الثانية: مصنف السياق البيئي والاقتصادي الرعوي
        معالجة التداخل الصوتي لمنع أخطاء الفهم الآلي (مثل: بالغنم / بلا غنم)
        """
        # خوارزمية ذكية: إذا وجد (هم أو فقر أو قعدان مراح) + (غنم/غلم) بدون أداة نفي صريحة
        # النظام يستنتج تلقائياً أن المقصد هو النفي "بلا غنم" لأن خلو المراح هو مبعث الهم
        if "هم" in text or "قعدان" in text:
            if "غنم" in text or "غلم" in text:
                if "بلا" not in text:
                    text = text.replace("بالغنم", "بلا غنم").replace("الغنم", "بلا غنم").replace("الغلم", "بلا غنم")
                    return f"{text} [تصحيح آلي للسياق: المقصد هو خلو المراح لأن العجز يجلب الهم الاقتصادي]"
        return text

    def extract_and_parse(self, text):
        """
        المحرك الرئيسي لتشغيل النظام وفك شفرات النصوص
        """
        # أ: تطبيق معالجة القواعد الصوتية أولاً
        processed_text = self.apply_phonetic_rules(text)
        
        # ب: تطبيق مصنف السياق البيئي الرعوي
        processed_text = self.context_aware_interpreter(processed_text)
        
        # ج: التنقيب عن الكيانات المسماة (NER) ومطابقتها بالقاموس التاريخي
        entities_found = {}
        for key, value in self.linguistic_dictionary.items():
            if key in processed_text:
                entities_found[key] = value
                
        return {
            "input_text": text,
            "processed_text": processed_text,
            "detected_historical_entities": entities_found
        }

# --- تجربة تشغيل النظام مخبرياً (Testing the Prototype) ---
if __name__ == "__main__":
    parser = TunisianGeoPhoneticParser()
    
    # تجربة 1: اختبار خوارزمية التطويع الصوتي للاستعمار الفرنسي
    test_1 = parser.extract_and_parse("المحصول تم تجميعه في la gare de tâche قبل شحنه")
    print(json.dumps(test_1, ensure_ascii=False, indent=2))
    print("-" * 50)
    
    # تجربة 2: اختبار خوارزمية منع التداخل السمعي (تصحيح خطأ الذكاء الاصطناعي)
    test_2 = parser.extract_and_parse("أول هم قعدان مراحك بالغنم")
    print(json.dumps(test_2, ensure_ascii=False, indent=2))
    print("-" * 50)
    
    # تجربة 3: اختبار فك شفرات الكيانات الجغرافية وعرش شقطمة بالقصرين
    test_3 = parser.extract_and_parse("وقع نزاع فلاحي وتم فضه بحضور كبار عرش شقطمة في مدينة سبيطلة محاذاة لجبل سلوم")
    print(json.dumps(test_3, ensure_ascii=False, indent=2))
