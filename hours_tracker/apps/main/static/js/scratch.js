






$(document).ready(function () {
    

    // $("form#addUser").submit(function () {
    //     var nameInput = $('input[name="name"]').val().trim();
    //     var addressInput = $('input[name="address"]').val().trim();
    //     var ageInput = $('input[name="age"]').val().trim();
    //     if (nameInput && addressInput && ageInput) {
    //         // Create Ajax Call
    //         $.ajax({
    //             url: '{% url "crud_app_create" %}',
    //             data: {
    //                 'name': nameInput,
    //                 'address': addressInput,
    //                 'age': ageInput
    //             },
    //             dataType: 'json',
    //             success: function (data) {
    //                 if (data.user) {
    //                     appendToUsrTable(data.user);
    //                 }
    //             }
    //         });
    //     } else {
    //         alert("All fields must have a valid value.");
    //     }
    //     $("form#addUser").trigger("reset");
    //     return false;
    // });


    // function appendToUsrTable(user) {
    //     $("#userTable > tbody:last-child").append(`
    //     <tr id="user-${user.id}">
    //         <td class="userName" name="name">${user.name}</td>            
    //         '<td class="userAddress" name="address">${user.address}</td>
    //         '<td class="userAge" name="age">${user.age}</td>
    //         '<td align="center">
    //             <button class="btn btn-success form-control" onClick="editUser(${user.id})" data-toggle="modal" data-target="#myModal")">EDIT</button>
    //         </td>
    //         <td align="center">
    //             <button class="btn btn-danger form-control" onClick="deleteUser(${user.id})">DELETE</button>
    //         </td>
    //     </tr>
    // `);
    // };


    // Create Django Ajax Call
    $("form#updateAssignment").submit(function () {
        var assignment_nameInput = $('input[name="assignment_name"]').val().trim();
        var due_dateInput = $('input[name="due_date"]').val().trim();
        var min_hoursInput = $('input[name="min_hours"]').val().trim();
        var max_hoursInput = $('input[name="max_hours"]').val().trim();
        var collection_idInput = $('input[name="collection_id"]').val().trim();
        var descriptionInput = $('input[name="description"]').val().trim();
        var priorityInput = $('input[name="priority"]').val().trim();
        $.ajax({
            url: '/update_assignment/',
            data: {
                'assignment_name': assignment_nameInput,
                'due_date': due_dateInput,
                'min_hours': min_hoursInput,
                'max_hours': max_hoursInput,
                'collection_id': collection_idInput,
                'description': descriptionInput,
                'priority': priorityInput,
            },
            dataType: 'json',
            success: function (data) {
                if (data.new_assignment) {
                    updateToAssignmentTable(data.new_assignment);      
                }
            }
        });
        } else {
            alert("All fields must have a valid value.");
        }
        $('form#updateAssignment').trigger("reset");
        $('#myModal').modal('hide');
        return false;
    });


    // Update Django Ajax Call    Set up no working
    function editAssignment(id) {
        if (id) {
            tr_id = "#assignment-" + id;
            assignment_name = $(tr_id).find(".assignmentName").text();
            console.log(assignment_name);
            due_date = $(tr_id).find(".assignmentDueDate").text();
            min_hours = $(tr_id).find(".assignmentMin").text();
            max_hours = $(tr_id).find(".assignmentMax").text();
            collection = $(tr_id).find(".assignmentCollection").text();
            description = $(tr_id).find(".assignmentDescription").text();
            priority = $(tr_id).find(".assignmentPriority").text();
            $('#assignment_form_id').val(id);
            $('#assignment_form_name').val(assignment_name);
            $('#assignment_form_due_date').val(due_date);
            $('#assignment_form_min_hours').val(min_hours);
            $('#assignment_form_max_hours').val(max_hours);
            $('#assignment_form_collection').val(collection);
            $('#assignment_form_description').val(description);
            $('#assignment_form_priority').val(priority);
        }
    }


    function updateToUserTabel(user) {
        $("#userTable #user-" + user.id).children(".userData").each(function () {
            var attr = $(this).attr("name");
            if (attr == "name") {
                $(this).text(user.name);
            } else if (attr == "address") {
                $(this).text(user.address);
            } else {
                $(this).text(user.age);
            }
        });
    }


// Delete Django Ajax Call
    function deleteUser(id) {
        var action = confirm("Are you sure you want to delete this user?");
        if (action != false) {
            $.ajax({
                url: '{% url "crud_app_delete" %}',
                data: {
                    'id': id,
                },
                dataType: 'json',
                success: function (data) {
                    if (data.deleted) {
                        $("#userTable #user-" + id).remove();
                    }
                }
            });
        }
    }

});











