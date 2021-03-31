// $(document).ready() {
//     $("form#updateAssignment").submit(function () {
//         var assignment_nameInput = $('input[name="assignment_name"]').val().trim();
//         var due_dateInput = $('input[name="due_date"]').val().trim();
//         var min_hoursInput = $('input[name="min_hours"]').val().trim();
//         var max_hoursInput = $('input[name="max_hours"]').val().trim();
//         var collection_idInput = $('input[name="collection_id"]').val().trim();
//         var descriptionInput = $('input[name="description"]').val().trim();
//         var priorityInput = $('input[name="priority"]').val().trim();
//         if (assignment_nameInput && due_dateInput){
//             $.ajax({
//                 url: '/update_assignment/',
//                 data: {
//                     'assignment_name': assignment_nameInput,
//                     'due_date': due_dateInput,
//                     'min_hours': min_hoursInput,
//                     'max_hours': max_hoursInput,
//                     'collection_id': collection_idInput,
//                     'description': descriptionInput,
//                     'priority': priorityInput,
//                 },
//                 dataType: 'json',
//                 success: function (data) {
//                     if (data.new_assignment) {
//                         updateToAssignmentTable(data.new_assignment);      
//                     }
//                 }
//             });
//             } else {
//                 alert("All fields must have a valid value.");
//             }
//             $('form#updateAssignment').trigger("reset");
//             $('#myModal').modal('hide');
//             return false;
//     });

//     // Update Django Ajax Call    Set up no working
//     function editAssignment(id) {
//         if (id) {
//             tr_id = "#assignment-" + id;
//             assignment_name = $(tr_id).find(".assignmentName").text();
//             console.log(assignment_name);
//             due_date = $(tr_id).find(".assignmentDueDate").text();
//             min_hours = $(tr_id).find(".assignmentMin").text();
//             max_hours = $(tr_id).find(".assignmentMax").text();
//             collection = $(tr_id).find(".assignmentCollection").text();
//             description = $(tr_id).find(".assignmentDescription").text();
//             priority = $(tr_id).find(".assignmentPriority").text();
//             $('#assignment_form_id').val(id);
//             $('#assignment_form_name').val(assignment_name);
//             $('#assignment_form_due_date').val(due_date);
//             $('#assignment_form_min_hours').val(min_hours);
//             $('#assignment_form_max_hours').val(max_hours);
//             $('#assignment_form_collection').val(collection);
//             $('#assignment_form_description').val(description);
//             $('#assignment_form_priority').val(priority);
//         }
//     }


//     function updateToAssignmentTable(user) {
//         $("#userTable #user-" + user.id).children(".userData").each(function () {
//             var attr = $(this).attr("name");
//             if (attr == "name") {
//                 $(this).text(user.name);
//             } else if (attr == "address") {
//                 $(this).text(user.address);
//             } else {
//                 $(this).text(user.age);
//             }
//         });
//     }


//         function assignmentDelete(id) {
//         console.log('fajitas')
//         var action = confirm("Are you sure you want to delete this assignment?");
//         if (action != false) {
//             console.log('Jelly bean')
//             $.ajax({
//                 url: '/delete_assignment',
//                 data: {
//                     'id': id,
//                 },
//                 dataType: 'json',
//                 success: function (data) {
//                     if (data.deleted) {
//                         console.log('made it')
//                         $("#assignments_table #assignment-" + id).remove();
//                     }
//                 }
//             });
//         }
//     }

