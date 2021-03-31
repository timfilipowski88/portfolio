$(document).ready(function () {
    
    // add assignment, needs success or failure json responses 
    $("form#add_assignment").submit(function(){
        var assignment_nameInput = $('input[name="assignment_name"]').val().trim();
        var due_dateInput = $('input[name="due_date"]').val().trim();
        var min_hoursInput = $('input[name="min_hours"]').val().trim();
        var max_hoursInput = $('input[name="max_hours"]').val().trim();
        var collection_idInput = $('input[name="collection_id"]').val().trim();
        var descriptionInput = $('input[name="description"]').val().trim();
        var priorityInput = $('input[name="priority"]').val().trim();
        $.ajax({
            url: '/main/add_assignment/',
            method: 'get',
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
                    appendToAssignmentTable(data.new_assignment);      
                }
            }
        });
        $("form#add_assignment").trigger("reset");
        return false;
    });
    
    // append to Assignment table function
    function appendToAssignmentTable (new_assignment) {
        $("#assignments_table > tbody:last-child").append(`
        <tr id="assignment-${new_assignment.id}">
            <td class="assignmentName assignmentData" name="name">${new_assignment.name}</td>
            <td class="assignmentDueDate assignmentData" name="due_date">${new_assignment.due_date}|date:'Y-m-d'</td>
            <td class="assignmentCollection assignmentData" name="collection">${new_assignment.collection.name}</td>
            <td class="assignmentMin assignmentData" name="min_hours">${new_assignment.min_hours}</td>
            <td class="assignmentMax assignmentData" name="max_hours">${new_assignment.max_hours}</td>
            <td class="assignmentPriority assignmentData" name="priority">${new_assignment.priority}</td>
            <td align="center">
                <button class="btn btn-secondary form-control" onClick="editAssignment(${new_assignment.id})" data-toggle="modal" data-target="assignmentModal">EDIT</button>
            </td>
            <td align="center">
                <button class="btn btn-success" onClick="changeComplete(${new_assignment.id})">COMPLETE</button>
            </td>
            <td align="center">
                <button class="btn btn-danger form-control" onClick="deleteAssignment(${new_assignment.id})">DELETE</button>   
            </td>
        </tr>
        `);
    }
});






    // fill out collections in collections tab table when nav button is clicked
// $('#pills-collections-tab').on("click", function(res){
//     console.log('hello world')
//     $.ajax({
//         url: '/main/get_collection_form',
//         method: 'GET',
//         success: function(res) {
//             console.log(res)
//             $('#collections_table_body').html(res)
//         }
//     })
// });
    // fill out assignments in assignments tab table when nav button is clicked
// $('#pills-assignments-tab').on("click", function(res){
//     console.log('hello world')
//     $.ajax({
//         url: '/main/get_assignment_form',
//         method: 'GET',
//         success: function(res) {
//             console.log(res)
//             $('#assignments_table_body').html(res)
//         }
//     })
// });
    
    // add collection
        // $('#add_collection').submit(function(e){
        //     e.preventDefault()
        //     $.ajax({
        //         url: '/main/add_collection/',
        //         method: 'POST',
        //         data: $(this).serialize(),
        //         success: function(res){
        //             $('#collections_table_body').append(res)
        //         }
        //     })
        // });
    
    //  update assignment
        // $('.update_assignment').submit(function(e){
        //     e.preventDefault()
        //     $.ajax({
        //         url: "{% url 'update_assigment' %}",
        //         method: 'POST',
        //         data: $(this).serialize(res),
        //         success: function(res){
        //             $('#assignments_table_body').html(res)
        //         }
        //     })
        // });
    
    

// Get future_date
// find all complete=False assignments_due with due_date less than future date
// get days_available, if null equal to total number of days between date_now and future_date
// Get total_min and total_max
// Average those assignments_due min and max values according to days_available
// context = { total_min, total_max, average_min, average_max, days_available, future_date}
