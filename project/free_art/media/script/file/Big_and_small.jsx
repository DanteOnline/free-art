//author: dante
//http://danteonline.pythonanywhere.com


//копируем объект и возвращаем набор объектов
//obj - объект, который мы копируем
//count - итоговое количество
function get_copy_objects(obj, count)
{
	//создаем массив оъектов
	var objs = new Array();
	//добавляем в него сам объект
	objs.push(obj);
	//копируем объект count-1 раза
	for (i=0;i<count-1;++i)
	{
		D = obj.duplicate();
		objs.push(D);
	}
	return objs;
};

/*берем выделенный объект*/
selected_objects = app.activeDocument.selection;
//Если выделен 1 объект
if (selected_objects.length == 1)
{
	//получаем выделенный объект
	obj = selected_objects[0];
	//получаем документ
	document = app.activeDocument;
	//получаем размеры документа
	dh = document.height;
	dw = document.width;
	
	count = 9
	
	all_objects = get_copy_objects(obj, count);
	
	//первый объект по центру
	center_obj = all_objects[0];
	//ставим в центр
	center_obj.top = -(dh/2-center_obj.height/2);
	center_obj.left = dw/2-center_obj.width/2;
	//4 средних по бокам
	scale1 = prompt("Input percent for middle objects:",75);
	//1
	middle_object1 = all_objects[1];
	middle_object1.resize(scale1,scale1);
	//левый
	middle_object1.top = -(dh/2-middle_object1.height/2);
	middle_object1.left = -middle_object1.width/2;
	//2
	middle_object2 = all_objects[2];
	middle_object2.resize(scale1,scale1);
	//правый
	middle_object2.top = -(dh/2-middle_object2.height/2);
	middle_object2.left = dw-middle_object2.width/2;
	//3
	middle_object3 = all_objects[3];
	middle_object3.resize(scale1,scale1);
	//верхний
	middle_object3.top = middle_object3.height/2;
	middle_object3.left = dw/2-middle_object3.width/2;
	//4
	middle_object4 = all_objects[4];
	middle_object4.resize(scale1,scale1);
	//нижний
	middle_object4.top = -(dh-middle_object4.height/2);
	middle_object4.left = dw/2-middle_object4.width/2;
	
	//4 маленьких
	//процент для маленьких
	scale2 = prompt("Input percent for small objects:",35);
	//1
	small_object1 = all_objects[5];
	small_object1.resize(scale2,scale2);
	//верхний левый
	var top = (middle_object3.top - center_obj.top)/2-small_object1.height/2;
	small_object1.top = -top;
	var left = (center_obj.left - middle_object1.left)/2-small_object1.width/2;
	small_object1.left = left;
	//2
	small_object1 = all_objects[6];
	small_object1.resize(scale2,scale2);
	//верхинй правый
	var top = (middle_object3.top - center_obj.top)/2-small_object1.height/2;
	small_object1.top = -top;
	var left = (dw - (middle_object2.left - (center_obj.left + center_obj.width))/2) - middle_object2.width/2 - small_object1.width/2;
	small_object1.left = left;
	//3
	small_object1 = all_objects[7];
	small_object1.resize(scale2,scale2);
	//нижний левый
	var top = -dh+middle_object4.height/2+(dh - (-center_obj.top+center_obj.height+middle_object4.height/2))/2 + small_object1.height/2;
	small_object1.top = top;
	var left = (center_obj.left - middle_object1.left)/2-small_object1.width/2;
	small_object1.left = left;
	//4
	small_object1 = all_objects[8];
	small_object1.resize(scale2,scale2);
	//нижний правый
	var top = -dh+middle_object4.height/2+(dh - (-center_obj.top+center_obj.height+middle_object4.height/2))/2 + small_object1.height/2;
	small_object1.top = top;
	var left = (dw - (middle_object2.left - (center_obj.left + center_obj.width))/2) - middle_object2.width/2 - small_object1.width/2;
	small_object1.left = left;
}
else{
	alert("Выделите только один объект!");
}


