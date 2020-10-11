
#kendi yazdıgımız faktoriyel isimli modülü yada kütüphanemizi
import faktoriyel
#oluşturulan modüle erişmek için modül ismi ardından nokta ve ardından modül içindeki fonk vs yazılmalıdır
print(faktoriyel.fak(6))
faktoriyel.fak(3)
#import modülü uzun ise onu as operatörü ile kısa hale getirebiliriz faktoriyel artık fak olarak çağrılabilir.
import faktoriyel as fak
fak.fak(4)
print(fak.__name__)   #kısaltılmış olan modülün tam olarak ismini ögrenmek için
#oluşturulan modülün içerisindeki sembolleri(fonksiyonları) içe aktarma yapılabilir.
from faktoriyel import fakto, fak
#artık fakto ve fak isimli fonksiyonlara dogrudan erişilebilir.
fak(7)
print(fakto(5))
#eğer modülün içerisinde çok simge fonksiyon var ise * varyant ile içe aktarma yapılabilir.
from faktoriyel import *
fak(5)
#sonuc olarak tekrar tekrar fonksiyon yada simgeleri kopyalmaya gerek kalmamaktadır. Bu şekilde işlemler hızlanır ve
#takım çalışmasına destek sağlanır.

#Pythonda her modül interpreter(tercüman)da oturumun başına yanlızca bir kez içe aktarılır. Eğer modülde
#değişiklik yaparsanız interpreterınızı yenilemeniz gerekir yada importlib.reload(modulismi) kullanılır.
#yazılan tercüman Modüllerde yapılan değişikleri

import importlib; importlib.reload( faktoriyel )