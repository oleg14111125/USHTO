from duty.objects import dp, MySignalEvent
# fixed bugs:
# vk: http://vk.com/id194861150
# github: https://github.com/Alex1249
eng = u"~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
rus = u"ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"
# TODO: каво нахуй
fix={'𝔸': '&#38;#120120;', '𝔹': '&#38;#120121;', '𝔻': '&#38;#120123;', '𝔼': '&#38;#120124;', '𝔽': '&#38;#120125;', '𝔾': '&#38;#120126;', '𝕀': '&#38;#120128;', '𝕁': '&#38;#120129;', '𝕂': '&#38;#120130;', '𝕃': '&#38;#120131;', '𝕄': '&#38;#120132;', '𝕆': '&#38;#120134;', '𝕊': '&#38;#120138;', '𝕋': '&#38;#120139;', '𝕌': '&#38;#120140;', '𝕍': '&#38;#120141;', '𝕎': '&#38;#120142;', '𝕏': '&#38;#120143;', '𝕐': '&#38;#120144;', '𝙰': '&#38;#120432;', '𝙱': '&#38;#120433;', '𝙲': '&#38;#120434;', '𝙳': '&#38;#120435;', '𝙴': '&#38;#120436;', '𝙵': '&#38;#120437;', '𝙶': '&#38;#120438;', '𝙷': '&#38;#120439;', '𝙸': '&#38;#120440;', '𝙹': '&#38;#120441;', '𝙺': '&#38;#120442;', '𝙻': '&#38;#120443;', '𝙽': '&#38;#120445;', '𝙾': '&#38;#120446;', '𝙿': '&#38;#120447;', '𝚀': '&#38;#120448;', '𝚁': '&#38;#120449;', '𝚂': '&#38;#120450;', '𝚃': '&#38;#120451;', '𝚄': '&#38;#120452;', '𝚅': '&#38;#120453;', '𝚆': '&#38;#120454;', '𝚇': '&#38;#120455;', '𝚈': '&#38;#120456;', '𝚉': '&#38;#120457;', '𝒜': '&#38;#119964;', '𝒞': '&#38;#119966;', '𝒟': '&#38;#119967;', '𝒢': '&#38;#119970;', '𝒥': '&#38;#119973;', '𝒦': '&#38;#119974;', '𝒩': '&#38;#119977;', '𝒪': '&#38;#119978;', '𝒫': '&#38;#119979;', '𝒬': '&#38;#119980;', '𝒮': '&#38;#119982;', '𝒯': '&#38;#119983;', '𝒰': '&#38;#119984;', '𝒱': '&#38;#119985;', '𝒲': '&#38;#119986;', '𝒳': '&#38;#119987;', '𝒴': '&#38;#119988;', '𝒵': '&#38;#119989;', '𝓐': '&#38;#120016;', '𝓑': '&#38;#120017;', '𝓒': '&#38;#120018;', '𝓓': '&#38;#120019;', '𝓔': '&#38;#120020;', '𝓕': '&#38;#120021;', '𝓖': '&#38;#120022;', '𝓗': '&#38;#120023;', '𝓘': '&#38;#120024;', '𝓙': '&#38;#120025;', '𝓚': '&#38;#120026;', '𝓛': '&#38;#120027;', '𝓜': '&#38;#120028;', '𝓝': '&#38;#120029;', '𝓞': '&#38;#120030;', '𝓟': '&#38;#120031;', '𝓠': '&#38;#120032;', '𝓡': '&#38;#120033;', '𝓢': '&#38;#120034;', '𝓣': '&#38;#120035;', '𝓤': '&#38;#120036;', '𝓥': '&#38;#120037;', '𝓦': '&#38;#120038;', '𝓧': '&#38;#120039;', '𝓨': '&#38;#120040;', '𝓩': '&#38;#120041;', '𝐀': '&#38;#119808;', '𝐁': '&#38;#119809;', '𝐂': '&#38;#119810;', '𝐃': '&#38;#119811;', '𝐄': '&#38;#119812;', '𝐅': '&#38;#119813;', '𝐆': '&#38;#119814;', '𝐇': '&#38;#119815;', '𝐈': '&#38;#119816;', '𝐉': '&#38;#119817;', '𝐊': '&#38;#119818;', '𝐋': '&#38;#119819;', '𝐌': '&#38;#119820;', '𝐍': '&#38;#119821;', '𝐎': '&#38;#119822;', '𝐏': '&#38;#119823;', '𝐐': '&#38;#119824;', '𝐑': '&#38;#119825;', '𝐒': '&#38;#119826;', '𝐓': '&#38;#119827;', '𝐔': '&#38;#119828;', '𝐕': '&#38;#119829;', '𝐖': '&#38;#119830;', '𝐗': '&#38;#119831;', '𝐘': '&#38;#119832;', '𝐙': '&#38;#119833;', '𝐴': '&#38;#119860;', '𝐵': '&#38;#119861;', '𝐶': '&#38;#119862;', '𝐷': '&#38;#119863;', '𝐸': '&#38;#119864;', '𝐹': '&#38;#119865;', '𝐺': '&#38;#119866;', '𝐻': '&#38;#119867;', '𝐼': '&#38;#119868;', '𝐽': '&#38;#119869;', '𝐾': '&#38;#119870;', '𝐿': '&#38;#119871;', '𝑀': '&#38;#119872;', '𝑁': '&#38;#119873;', '𝑂': '&#38;#119874;', '𝑃': '&#38;#119875;', '𝑄': '&#38;#119876;', '𝑅': '&#38;#119877;', '𝑆': '&#38;#119878;', '𝑇': '&#38;#119879;', '𝑈': '&#38;#119880;', '𝑉': '&#38;#119881;', '𝑊': '&#38;#119882;', '𝑋': '&#38;#119883;', '𝑌': '&#38;#119884;', '𝑍': '&#38;#119885;', '𝑨': '&#38;#119912;', '𝑩': '&#38;#119913;', '𝑪': '&#38;#119914;', '𝑫': '&#38;#119915;', '𝑬': '&#38;#119916;', '𝑭': '&#38;#119917;', '𝑮': '&#38;#119918;', '𝑯': '&#38;#119919;', '𝑰': '&#38;#119920;', '𝑱': '&#38;#119921;', '𝑲': '&#38;#119922;', '𝑳': '&#38;#119923;', '𝑴': '&#38;#119924;', '𝑵': '&#38;#119925;', '𝑶': '&#38;#119926;', '𝑷': '&#38;#119927;', '𝑸': '&#38;#119928;', '𝑹': '&#38;#119929;', '𝑺': '&#38;#119930;', '𝑻': '&#38;#119931;', '𝑼': '&#38;#119932;', '𝑽': '&#38;#119933;', '𝑾': '&#38;#119934;', '𝑿': '&#38;#119935;', '𝒀': '&#38;#119936;', '𝒁': '&#38;#119937;', '𝔄': '&#38;#120068;', '𝔅': '&#38;#120069;', '𝔇': '&#38;#120071;', '𝔈': '&#38;#120072;', '𝔉': '&#38;#120073;', '𝔊': '&#38;#120074;', '𝔍': '&#38;#120077;', '𝔎': '&#38;#120078;', '𝔏': '&#38;#120079;', '𝔐': '&#38;#120080;', '𝔑': '&#38;#120081;', '𝔒': '&#38;#120082;', '𝔓': '&#38;#120083;', '𝔔': '&#38;#120084;', '𝔖': '&#38;#120086;', '𝔗': '&#38;#120087;', '𝔘': '&#38;#120088;', '𝔙': '&#38;#120089;', '𝔚': '&#38;#120090;', '𝔛': '&#38;#120091;', '𝔜': '&#38;#120092;', '𝕬': '&#38;#120172;', '𝕭': '&#38;#120173;', '𝕮': '&#38;#120174;', '𝕯': '&#38;#120175;', '𝕰': '&#38;#120176;', '𝕱': '&#38;#120177;', '𝕲': '&#38;#120178;', '𝕳': '&#38;#120179;', '𝕴': '&#38;#120180;', '𝕵': '&#38;#120181;', '𝕶': '&#38;#120182;', '𝕷': '&#38;#120183;', '𝕸': '&#38;#120184;', '𝕹': '&#38;#120185;', '𝕺': '&#38;#120186;', '𝕻': '&#38;#120187;', '𝕼': '&#38;#120188;', '𝕽': '&#38;#120189;', '𝕾': '&#38;#120190;', '𝕿': '&#38;#120191;', '𝖀': '&#38;#120192;', '𝖁': '&#38;#120193;', '𝖂': '&#38;#120194;', '𝖃': '&#38;#120195;', '𝖄': '&#38;#120196;', '𝖅': '&#38;#120197;', '𝕒': '&#38;#120146;', '𝕓': '&#38;#120147;', '𝕔': '&#38;#120148;', '𝕕': '&#38;#120149;', '𝕖': '&#38;#120150;', '𝕗': '&#38;#120151;', '𝕘': '&#38;#120152;', '𝕙': '&#38;#120153;', '𝕚': '&#38;#120154;', '𝕛': '&#38;#120155;', '𝕜': '&#38;#120156;', '𝕝': '&#38;#120157;', '𝕞': '&#38;#120158;', '𝕟': '&#38;#120159;', '𝕠': '&#38;#120160;', '𝕡': '&#38;#120161;', '𝕢': '&#38;#120162;', '𝕣': '&#38;#120163;', '𝕤': '&#38;#120164;', '𝕥': '&#38;#120165;', '𝕦': '&#38;#120166;', '𝕧': '&#38;#120167;', '𝕨': '&#38;#120168;', '𝕩': '&#38;#120169;', '𝕪': '&#38;#120170;', '𝕫': '&#38;#120171;','𝚊': '&#38;#120458;', '𝚋': '&#38;#120459;', '𝚌': '&#38;#120460;', '𝚍': '&#38;#120461;', '𝚎': '&#38;#120462;', '𝚏': '&#38;#120463;', '𝚐': '&#38;#120464;', '𝚑': '&#38;#120465;', '𝚒': '&#38;#120466;', '𝚓': '&#38;#120467;', '𝚔': '&#38;#120468;', '𝚕': '&#38;#120469;', '𝚖': '&#38;#120470;', '𝚗': '&#38;#120471;', '𝚘': '&#38;#120472;', '𝚙': '&#38;#120473;', '𝚚': '&#38;#120474;', '𝚛': '&#38;#120475;', '𝚜': '&#38;#120476;', '𝚝': '&#38;#120477;', '𝚞': '&#38;#120478;', '𝚟': '&#38;#120479;', '𝚠': '&#38;#120480;', '𝚡': '&#38;#120481;', '𝚢': '&#38;#120482;', '𝚣': '&#38;#120483;', '𝒶': '&#38;#119990;', '𝒷': '&#38;#119991;', '𝒸': '&#38;#119992;', '𝒹': '&#38;#119993;', '𝒻': '&#38;#119995;', '𝒽': '&#38;#119997;', '𝒾': '&#38;#119998;', '𝒿': '&#38;#119999;', '𝓀': '&#38;#120000;', '𝓁': '&#38;#120001;', '𝓂': '&#38;#120002;', '𝓃': '&#38;#120003;', '𝓅': '&#38;#120005;', '𝓆': '&#38;#120006;', '𝓇': '&#38;#120007;', '𝓈': '&#38;#120008;', '𝓉': '&#38;#120009;', '𝓊': '&#38;#120010;', '𝓋': '&#38;#120011;', '𝓌': '&#38;#120012;', '𝓍': '&#38;#120013;', '𝓎': '&#38;#120014;', '𝓏': '&#38;#120015;', '𝓪': '&#38;#120042;', '𝓫': '&#38;#120043;', '𝓬': '&#38;#120044;', '𝓭': '&#38;#120045;', '𝓮': '&#38;#120046;', '𝓯': '&#38;#120047;', '𝓰': '&#38;#120048;', '𝓱': '&#38;#120049;', '𝓲': '&#38;#120050;', '𝓳': '&#38;#120051;', '𝓴': '&#38;#120052;', '𝓵': '&#38;#120053;', '𝓶': '&#38;#120054;', '𝓷': '&#38;#120055;', '𝓸': '&#38;#120056;', '𝓹': '&#38;#120057;', '𝓺': '&#38;#120058;', '𝓻': '&#38;#120059;', '𝓼': '&#38;#120060;', '𝓽': '&#38;#120061;', '𝓾': '&#38;#120062;', '𝓿': '&#38;#120063;', '𝔀': '&#38;#120064;', '𝔁': '&#38;#120065;', '𝔂': '&#38;#120066;', '𝔃': '&#38;#120067;', '𝐚': '&#38;#119834;', '𝐛': '&#38;#119835;', '𝐜': '&#38;#119836;', '𝐝': '&#38;#119837;', '𝐞': '&#38;#119838;', '𝐟': '&#38;#119839;', '𝐠': '&#38;#119840;', '𝐡': '&#38;#119841;','𝐢': '&#38;#119842;', '𝐣': '&#38;#119843;', '𝐤': '&#38;#119844;', '𝐥': '&#38;#119845;', '𝐦': '&#38;#119846;', '𝐧': '&#38;#119847;', '𝐨': '&#38;#119848;', '𝐩': '&#38;#119849;', '𝐪': '&#38;#119850;', '𝐫': '&#38;#119851;', '𝐬': '&#38;#119852;', '𝐭': '&#38;#119853;', '𝐮': '&#38;#119854;', '𝐯': '&#38;#119855;', '𝐰': '&#38;#119856;', '𝐱': '&#38;#119857;', '𝐲': '&#38;#119858;', '𝐳': '&#38;#119859;', '𝑎': '&#38;#119886;', '𝑏': '&#38;#119887;', '𝑐': '&#38;#119888;', '𝑑': '&#38;#119889;', '𝑒': '&#38;#119890;', '𝑓': '&#38;#119891;', '𝑔': '&#38;#119892;', '𝑖': '&#38;#119894;', '𝑗': '&#38;#119895;', '𝑘': '&#38;#119896;', '𝑙': '&#38;#119897;', '𝑚': '&#38;#119898;', '𝑛': '&#38;#119899;', '𝑜': '&#38;#119900;', '𝑝': '&#38;#119901;', '𝑞': '&#38;#119902;', '𝑟': '&#38;#119903;', '𝑠': '&#38;#119904;', '𝑡': '&#38;#119905;', '𝑢': '&#38;#119906;', '𝑣': '&#38;#119907;', '𝑤': '&#38;#119908;', '𝑥': '&#38;#119909;', '𝑦': '&#38;#119910;', '𝑧': '&#38;#119911;', '𝒂': '&#38;#119938;', '𝒃': '&#38;#119939;', '𝒄': '&#38;#119940;', '𝒅': '&#38;#119941;', '𝒆': '&#38;#119942;', '𝒇': '&#38;#119943;', '𝒈': '&#38;#119944;', '𝒉': '&#38;#119945;', '𝒊': '&#38;#119946;', '𝒋': '&#38;#119947;', '𝒌': '&#38;#119948;', '𝒍': '&#38;#119949;', '𝒎': '&#38;#119950;', '𝒏': '&#38;#119951;', '𝒐': '&#38;#119952;', '𝒑': '&#38;#119953;', '𝒒': '&#38;#119954;', '𝒓': '&#38;#119955;', '𝒔': '&#38;#119956;', '𝒕': '&#38;#119957;', '𝒖': '&#38;#119958;', '𝒗': '&#38;#119959;', '𝒘': '&#38;#119960;', '𝒙': '&#38;#119961;', '𝒚': '&#38;#119962;', '𝒛': '&#38;#119963;', '𝔞': '&#38;#120094;', '𝔟': '&#38;#120095;', '𝔠': '&#38;#120096;', '𝔡': '&#38;#120097;', '𝔢': '&#38;#120098;', '𝔣': '&#38;#120099;', '𝔤': '&#38;#120100;', '𝔥': '&#38;#120101;', '𝔦': '&#38;#120102;', '𝔧': '&#38;#120103;', '𝔨': '&#38;#120104;', '𝔩': '&#38;#120105;', '𝔪': '&#38;#120106;', '𝔫': '&#38;#120107;', '𝔬': '&#38;#120108;', '𝔭': '&#38;#120109;', '𝔮': '&#38;#120110;', '𝔯': '&#38;#120111;', '𝔰': '&#38;#120112;', '𝔱': '&#38;#120113;', '𝔲': '&#38;#120114;', '𝔳': '&#38;#120115;', '𝔴': '&#38;#120116;', '𝔵': '&#38;#120117;', '𝔶': '&#38;#120118;', '𝔷': '&#38;#120119;', '𝖆': '&#38;#120198;', '𝖇': '&#38;#120199;', '𝖈': '&#38;#120200;', '𝖉': '&#38;#120201;', '𝖊': '&#38;#120202;', '𝖋': '&#38;#120203;', '𝖌': '&#38;#120204;', '𝖍': '&#38;#120205;', '𝖎': '&#38;#120206;', '𝖏': '&#38;#120207;', '𝖐': '&#38;#120208;', '𝖑': '&#38;#120209;', '𝖒': '&#38;#120210;', '𝖓': '&#38;#120211;', '𝖔': '&#38;#120212;', '𝖕': '&#38;#120213;', '𝖖': '&#38;#120214;', '𝖗': '&#38;#120215;', '𝖘': '&#38;#120216;', '𝖙': '&#38;#120217;', '𝖚': '&#38;#120218;', '𝖛': '&#38;#120219;', '𝖜': '&#38;#120220;', '𝖝': '&#38;#120221;', '𝖞': '&#38;#120222;', '𝖟': '&#38;#120223;', '𝙼':'&#38;#120444;'}

fonts = {
    '1': u"~!@#$%^&𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡[]𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝;'𝕫𝕩𝕔𝕧𝕓𝕟𝕞,./ℚ𝕎𝔼ℝ𝕋𝕐𝕌𝕀𝕆ℙ{}𝔸𝕊𝔻𝔽𝔾ℍ𝕁𝕂𝕃:\"|ℤ𝕏ℂ𝕍𝔹ℕ𝕄<>?",
    '2': u"~!@#$%^&𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙[]𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕;'𝚣𝚡𝚌𝚟𝚋𝚗𝚖,./𝚀𝚆𝙴𝚁𝚃𝚈𝚄𝙸𝙾𝙿{}𝙰𝚂𝙳𝙵𝙶𝙷𝙹𝙺𝙻:\"|𝚉𝚇𝙲𝚅𝙱𝙽𝙼<>?",
    '3': u"~!@#$%^&𝓆𝓌ℯ𝓇𝓉𝓎𝓊𝒾ℴ𝓅[]𝒶𝓈𝒹𝒻ℊ𝒽𝒿𝓀𝓁;'𝓏𝓍𝒸𝓋𝒷𝓃𝓂,./𝒬𝒲ℰℛ𝒯𝒴𝒰ℐ𝒪𝒫{}𝒜𝒮𝒟ℱ𝒢ℋ𝒥𝒦ℒ:\"|𝒵𝒳𝒞𝒱ℬ𝒩ℳ<>?",
    '4': u"~!@#$%^&𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹[]𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵;'𝔃𝔁𝓬𝓿𝓫𝓷𝓶,./𝓠𝓦𝓔𝓡𝓣𝓨𝓤𝓘𝓞𝓟{}𝓐𝓢𝓓𝓕𝓖𝓗𝓙𝓚𝓛:\"|𝓩𝓧𝓒𝓥𝓑𝓝𝓜<>?",
    '5': u"~¡@#$%^&bʍǝɹʇʎnᴉod[]ɐspɟƃɥɾʞl;'zxɔʌquɯ,./bʍǝɹʇʎnᴉod{}ɐspɟƃɥɾʞl:\"|zxɔʌquɯ<>¿",
    '6': u"~!@#$%^&ǫᴡᴇʀᴛʏᴜɪᴏᴘ[]ᴀsᴅғɢʜᴊᴋʟ;'ᴢxᴄᴠʙɴᴍ,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?",
    '7': u"~!@#$%^&ᑫᗯᗴᖇTYᑌIOᑭ[]ᗩՏᗪᖴᘜᕼᒍKᒪ;'ᘔ᙭ᑕᐯᗷᑎᗰ,./ᑫᗯᗴᖇTYᑌIOᑭ{}ᗩՏᗪᖴᘜᕼᒍKᒪ:\"|ᘔ᙭ᑕᐯᗷᑎᗰ<>?",
    '8': u"~!@#$%^&𝐪𝐰𝐞𝐫𝐭𝐲𝐮𝐢𝐨𝐩[]𝐚𝐬𝐝𝐟𝐠𝐡𝐣𝐤𝐥;'𝐳𝐱𝐜𝐯𝐛𝐧𝐦,./𝐐𝐖𝐄𝐑𝐓𝐘𝐔𝐈𝐎𝐏{}𝐀𝐒𝐃𝐅𝐆𝐇𝐉𝐊𝐋:\"|𝐙𝐗𝐂𝐕𝐁𝐍𝐌<>?",
    '9': u"~!@#$%^&𝑞𝑤𝑒𝑟𝑡𝑦𝑢𝑖𝑜𝑝[]𝑎𝑠𝑑𝑓𝑔ℎ𝑗𝑘𝑙;'𝑧𝑥𝑐𝑣𝑏𝑛𝑚,./𝑄𝑊𝐸𝑅𝑇𝑌𝑈𝐼𝑂𝑃{}𝐴𝑆𝐷𝐹𝐺𝐻𝐽𝐾𝐿:\"|𝑍𝑋𝐶𝑉𝐵𝑁𝑀<>?",
    '10': u"~!@#$%^&𝒒𝒘𝒆𝒓𝒕𝒚𝒖𝒊𝒐𝒑[]𝒂𝒔𝒅𝒇𝒈𝒉𝒋𝒌𝒍;'𝒛𝒙𝒄𝒗𝒃𝒏𝒎,./𝑸𝑾𝑬𝑹𝑻𝒀𝑼𝑰𝑶𝑷{}𝑨𝑺𝑫𝑭𝑮𝑯𝑱𝑲𝑳:\"|𝒁𝑿𝑪𝑽𝑩𝑵𝑴<>?",
    '11': u"~!@#$%^&ⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅ[]ⒶⓈⒹⒻⒼⒽⒿⓀⓁ;'ⓏⓍⒸⓋⒷⓃⓂ,./ⓆⓌⒺⓇⓉⓎⓊⒾⓄⓅ{}ⒶⓈⒹⒻⒼⒽⒿⓀⓁ:\"|ⓏⓍⒸⓋⒷⓃⓂ<>?",
    '12': u"~!@#$%^&🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟[]🅐🅢🅓🅕🅖🅗🅙🅚🅛;'🅩🅧🅒🅥🅑🅝🅜,./🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟{}🅐🅢🅓🅕🅖🅗🅙🅚🅛:\"|🅩🅧🅒🅥🅑🅝🅜<>?",
    '13': u"~!@#$%^&🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿[]🄰🅂🄳🄵🄶🄷🄹🄺🄻;'🅉🅇🄲🅅🄱🄽🄼,./🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿{}🄰🅂🄳🄵🄶🄷🄹🄺🄻:\"|🅉🅇🄲🅅🄱🄽🄼<>?",
    '14': u"~!@#$%^&𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭[]𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩;'𝔷𝔵𝔠𝔳𝔟𝔫𝔪,./𝔔𝔚𝔈ℜ𝔗𝔜𝔘ℑ𝔒𝔓{}𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏:\"|ℨ𝔛ℭ𝔙𝔅𝔑𝔐<>?",
    '15': u"~!@#$%^&𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕[]𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑;'𝖟𝖝𝖈𝖛𝖇𝖓𝖒,./𝕼𝖂𝕰𝕽𝕿𝖄𝖀𝕴𝕺𝕻{}𝕬𝕾𝕯𝕱𝕲𝕳𝕵𝕶𝕷:\"|𝖅𝖃𝕮𝖁𝕭𝕹𝕸<>?"
    }

translit = u'ё|!|"|№|;|%|:|?|y|ts|u|k|e|n|g|sh|sch|z|kh||f|y|v|a|p|r|o|l|d|zh|e|ya|ch|s|m|i|t||b|yu|.|Y|TS|U|K|E|N|G|SH|SCH|Z|KH||F|Y|B|A|P|R|O|L|D|ZH|E|/|YA|CH|S|M|I|T||B|YU|'
translit = dict(zip(rus, translit.split('|')))


@dp.longpoll_event_register('конв', '-конв')
@dp.my_signal_event_register('конв', '-конв')
def conv_text(event: MySignalEvent) -> str:
    trans_table = dict(zip(eng, rus)) if event.command == 'конв' else dict(zip(rus, eng))
    s = ''
    if event.args:
        s = " ".join(event.args)
    if event.payload:
        s = s + '\n' + event.payload
    if event.reply_message:
        s = s + '\n' + event.reply_message['text']
    if event.msg['fwd_messages']:
        for i in event.msg['fwd_messages']:
            s += '\n\n' + i['text']

    if s == '':
        event.msg_op(2, 'Нет данных 🤦')
        return "ok"

    message = u''.join([trans_table.get(c, c) for c in s])
    event.msg_op(2, message, keep_forward_messages=1)
    return "ok"


@dp.longpoll_event_register('шрифты')
@dp.my_signal_event_register('шрифты')
def fonts_list(event: MySignalEvent) -> str:
    msg="""
    1. 𝕠𝕦𝕥𝕝𝕚𝕟𝕖 (outline)
    2. 𝚝𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛 (typewriter)
    3. 𝓈𝒸𝓇𝒾𝓅𝓉 (script)
    4. 𝓼𝓬𝓻𝓲𝓹𝓽_𝓫𝓸𝓵𝓭 (script_bold)
    5. uʍop_ǝpᴉsdn (upside_down)
    6. ᴛɪɴʏ_ᴄᴀᴘs (tiny_caps)
    7. ᑕOᗰIᑕ (comic)
    8. 𝐬𝐞𝐫𝐢𝐟_𝐛 (serif_b)
    9. 𝑠𝑒𝑟𝑖𝑓_𝑖 (serif_i)
    10. 𝒔𝒆𝒓𝒊𝒇_𝒃𝒊 (serif_bi)
    11. ⒸⒾⓇⒸⓁⒺⓈ (circles)
    12. 🅒🅘🅡🅒🅛🅔🅢_🅑 (circles_b)
    13. 🅂🅀🅄🄰🅁🄴🅂 (squares)
    14. 𝔤𝔬𝔱𝔥𝔦𝔠 (gothic)
    15. 𝖌𝖔𝖙𝖍𝖎𝖈_𝖇 (gothic_b)""".replace('    ', '')

    msgfix=  ''.join(fix.get(a, a) for a in msg)
    event.msg_op(2, msgfix)
    return "ok"


@dp.longpoll_event_register('шрифт')
@dp.my_signal_event_register('шрифт')
def fonts_convert(event: MySignalEvent) -> str:
    dest = None
    if event.args:
        if event.args[0] in fonts.keys():
            message = f'{" ".join(event.args[1:])}\n{event.payload}'
            dest = fonts[event.args[0]]
            s = ''.join(translit.get(c, c) for c in message)
            msg = u''.join(dict(zip(eng, dest)).get(c, c) for c in s)
            if event.args[0] == '5':
                msg = msg[::-1]
            msg = ''.join(fix.get(a, a) for a in msg)
    if dest is None:
        msg = """Просмотр списка шрифтов - .с шрифты
        \nКоманда для переделывания кмд:\n.с шрифт [номер]\n[текст]"""
    event.msg_op(2, msg, keep_forward_messages=1)
    return "ok"
