// $(function () {
//     $("#btnADD").click(function () {
//         //接收用户输入的列数据
//         // var id=prompt("ID：");
//         // var name=prompt("名字：");
//         // var jianjie=prompt("简介：");
//         // var banji=prompt("班级：");
//         // var teacher=prompt("老师：");

//         var id = document.getElementById("itemID").value;
//         var name = document.getElementById("itemName").value;
//         var jianjie = document.getElementById("itemJianjie").value;
//         var banji = document.getElementById("itemBanji").value;
//         var teacher = document.getElementById("itemTeacher").value;

//         //构建新行
//         var newRow = "<tr><td>" + id + "</td><td>" + name + "</td></tr>" + jianjie + "</td></tr>" + banji + "</td></tr>" + teacher + "</td></tr>";
//         //为表格追加新行
//         $("#tbody").append(newRow);
//     });
// })

// $("#btnADD").on('click', 'tr>td', function () {
//     // alert($(this).html());
//     var id = document.getElementById("itemID").Value;
//     var name = document.getElementById("itemName").Value;
//     var jianjie = document.getElementById("itemJianjie").Value;
//     var banji = document.getElementById("itemBanji").Value;
//     var teacher = document.getElementById("itemTeacher").Value;

//     //构建新行
//     var newRow = "<tr><td>" + id + "</td><td>" + name + "</td></tr>" + jianjie + "</td></tr>" + banji + "</td></tr>" + teacher + "</td></tr>";
//     //为表格追加新行
//     $("#newItem").appendChild(newRow);
// });

// 以上两种方式全部无效

// 获取table上的ID
// var id = $("#testTable").find("tr:last").find("td:first").text()
// 指定的位置使用,find("tr").eq(-1)

// json数据
var obj = [{ "ID": "1", "名字": "哦呢哦呢哦", "简介": "的就覅偶发的", "班级": "公社1602", "老师": "六千万" }, { "ID": "2", "名字": "林峰", "简介": "这个故事很棒", "班级": "公社1302", "老师": "二千万" }];

function addItem() {
    var id = document.getElementById("itemID").value;
    var name = document.getElementById("itemName").value;
    var jianjie = document.getElementById("itemJianjie").value;
    var banji = document.getElementById("itemBanji").value;
    var teacher = document.getElementById("itemTeacher").value;
    // console.log("ok")
    obj.push({ "ID": id, "名字": name, "简介": jianjie, "班级": banji, "老师": teacher });

    alert("ok")
}

// 删除元素,传入ID
function deleteItem(a) {
    $.each(obj, function (n, value) {
        if (value.ID == a) {
            obj.splice(n, 1); //删除第n个，并且只删除一个，返回删除的项，若是0，返回空数组
            alert(value.name)
        }
    })
    // console.log("ok")
}

function newIt() {
    var id = document.getElementById("itemID").value;
    var name = document.getElementById("itemName").value;
    var jianjie = document.getElementById("itemJianjie").value;
    var banji = document.getElementById("itemBanji").value;
    var teacher = document.getElementById("itemTeacher").value;

    // 处理输入的值
    // tip1:判断ID顺序使是否正确
    // 获取ID
    // var rankId = $("#testTable").find("tr:last").find("td:first").text();
    var rankId = $("#newItem").find("tr:last").find("td").eq(1).text();
    var IntRankId = parseInt(rankId); // 转换成数字类型
    if (id !== IntRankId + 1) {
        id = IntRankId + 1
    } else {
        alert("ID error!!!")
    };

    //构建新行
    // var newRow = "<tr><td><input type='checkbox' name='test'>" + id + "</td><td>" + name + "</td><td>" + jianjie + "</td><td style='text-overflow: ellipsis;overflow: hidden;'nowrap>" + banji + "</td><td>" + teacher + "</td></tr>";
    // $("#newItem").append(newRow);
    // var newRow = "<tr><td><input type='checkbox' name='test'></td><td>" + id + "</td><td>" + name + "</td><td>" + jianjie + "</td><td style='text-overflow: ellipsis;overflow: hidden;'nowrap>" + banji + "</td><td>" + teacher + "</td></tr>";
    // $("#newItem").append(newRow);

    var newRow = "<tr><td><input type='checkbox' name='test'></td><td id='item-ID'>" + id + "</td><td>" + name + "</td><td>" + jianjie + "</td><td style='text-overflow: ellipsis;overflow: hidden;'nowrap>" + banji + "</td><td>" + teacher + "</td></tr>";
    $("#newItem").append(newRow);

    // after添加在tbody后面第一个，append追加在最后

    // reset

}

//TODO：
// 删除行,更新ID（暂未想到，可能要重写逻辑）
function deleteIt() {
    $("input[name='test']:checked").each(function () { // 遍历选中的checkbox
        n = $(this).parents("tr").index() + 1;  // 获取checkbox所在行的顺序
        $("table#testTable").find("tr:eq(" + n + ")").remove(); //n为变量
    });
    // window.location.reload() //刷新页面

    // TOdo:  排列ID
    // 统计ID数量
    var IDList = $('tbody [id=item-ID]'); // 0,1,2,5,6
    var IDLength = IDList.length;

    for (i = 0; i <= IDLength; i++) {
        let IDValue = $('tbody [id=item-ID]').eq(i).text();
        // console.log(IDValue)
        // console.log(i)
        var IDIndex = i + 1
        // 替换部分
        $('tbody [id=item-ID]').eq(i).replaceWith("<td id='item-ID'>" + IDIndex + "</td>")
    }

}

function resetIt() {
    $("input").val("");
}